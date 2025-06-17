from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate ### (yeni uygulama)
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import json, csv
import sys  #Terminal çıktısını zorlamak için
from datetime import datetime, timedelta
from models import db, User, Visitor
from data_manager import load_users, save_users
from data_manager import save_visitors
from data_manager import delete_visitor_from_json
from flask import request
from sqlalchemy import func, or_
from flask import Response
from fpdf import FPDF


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gelistirme_anahtari' #sessıon bılgılerını tarayıcıda tutmak ıcın
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #database ne adında olucak
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db) ### (yeni uygulama)

login_manager = LoginManager(app)  #kullanıcı gereklı bır sayfa mevcut ıse: kısının gunluklerı gıbı
login_manager.login_view = 'login'  # gereklı gıurıs ıcın hangı rota kullanılsın? logın rotasına gıt

def export_users_to_json():
    with app.app_context():
        users = User.query.all()
        data = []
        for user in users:
            data.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password  # şifreler hashli şekilde yazılır, düz şifre değil-database baz alınarak
            })
        
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Kullanıcılar başarıyla users.json dosyasına kaydedildi!")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))    

# Ana kuralların tanımı
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        user_identifier = request.form.get('user_identifier')  #E-posta veya isim olabilir
        password = request.form.get('password')
        user = User.query.filter((User.email == user_identifier) | (User.name == user_identifier)).first()
        print("Veritabanında bulunan kullanıcı:", user)  #Kullanıcının olup olmadığını kontrol et
        sys.stdout.flush()

        if user:
            print("Girilen şifre:", password)
            print("Veritabanında kayıtlı şifre (hash):", user.password)
            print("Şifreler eşleşiyor mu?:", check_password_hash(user.password, password))
            sys.stdout.flush()

        if user and check_password_hash(user.password, password):
            remember = request.form.get('remember') == 'on'
            login_user(user, remember=remember)

            print("Giriş sonrası kullanıcı durumu:", current_user.is_authenticated)
            print("Yönlendirme yapılacak sayfa:", url_for('registervisitor'))
            sys.stdout.flush()
            
            flash("Giriş başarılı!", "success")
            return redirect(url_for('registervisitor'))  #Ziyaretçi paneline yönlendir

        flash("Hatalı giriş bilgileri!", "danger")
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/registervisitor', methods=['GET', 'POST']) #ziyaretçi kaydı
@login_required #Ziyaretçileri kaydetmek için önce giriş yapmalısınız
def registervisitor():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')
        date = datetime.today().date()  #güncel tarih
        time = datetime.now().time()  #güncel saat
        visitor_type = request.form.get('visitor_type') ######ziyaretçi türü (yeni alan)
        other_data = request.form.get('other_data')
        new_visitor = Visitor(name=name, surname=surname, phone=phone, date=date, time=time, visitor_type=visitor_type, other_data=other_data)
        db.session.add(new_visitor)
        db.session.commit()
        save_visitors(new_visitor)

        print("Ziyaretçi kayıt sayfasına erişildi.")
        sys.stdout.flush()


        flash("Ziyaretçi başarıyla kaydedildi!", "success")
        return redirect(url_for('dashboard'))  

    return render_template('registervisitor.html')

#####Ziyaretçi türüne göre erişim kısıtlaması (yeni alan)

@app.route("/check_access/<int:visitor_id>")
@login_required
def check_access(visitor_id):
    visitor = Visitor.query.get(visitor_id)

    if not visitor:
        flash("Ziyaretçi bulunamadı!", "danger")
        return redirect(url_for('dashboard'))

    current_hour = datetime.now().hour

    if visitor.visitor_type == "Tedarikçi" and current_hour > 18:
        flash("Erişim reddedildi: Çalışma saatleri dışında.", "danger")
        return redirect(url_for('dashboard'))
    elif visitor.visitor_type == "Misafir" and current_hour > 22:
        flash("Erişim reddedildi: Ziyaret saatleri sona erdi.", "danger")
        return redirect(url_for('dashboard'))
    else:
        flash("Erişim sağlandı.", "success")
        return redirect(url_for('dashboard'))

@app.route('/createaccount', methods=['GET', 'POST']) #yeni kullanıcı kayıt formu 
def createaccount():
    if request.method == 'POST': 
        name = request.form.get('name')
        email = request.form.get('email') #yeni kullanıcı kayıt formu e-postası
        password = request.form.get('password') #yeni kullanıcı kayıt formu için şifre
        confirm_password = request.form.get('confirm_password')

    # Şifreler eşleşiyor mu? Eğer eşleşmiyorsa hata mesajı göster.
                              
        if password != confirm_password: #Şifrelerin eşleşip eşleşmediğini kontrol edin
            flash("Şifreler eşleşmiyor! Lütfen tekrar deneyin.", "danger")
            return redirect(url_for('createaccount'))

        print("Yeni kullanıcı oluşturuluyor:", name, email)
        sys.stdout.flush()
        
        #Kullanıcının veritabanında zaten mevcut olup olmadığını kontrol edin
        if User.query.filter_by(email=email).first() or User.query.filter_by(name=name).first(): 
            flash('Bu e-posta zaten kayıtlı!', 'danger') #sayfa mesajları dondurme
            return redirect(url_for('createaccount'))
        
        users = load_users() #Kullanıcının `users.json` dosyasında zaten mevcut olup olmadığını kontrol edin
        if any(user["email"] == email for user in users):
            flash("Bu e-posta zaten kayıtlı!", "danger")
            return redirect(url_for("createaccount"))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        #Ayrıca `users.json`'a kaydedin
        users.append({"id": new_user.id, "name": name, "email": email, "password": hashed_password})  
        save_users(users) 

        print("Veritabanına kaydedilen yeni kullanıcı:", new_user)
        sys.stdout.flush()

        
        flash('Kayıt başarılı! Giriş yapabilirsiniz.', 'success') #sayfa mesajları dondurme
        return redirect(url_for('login'))
    return render_template('createaccount.html')


@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    query = request.args.get('q', '').strip()
    date_filter = request.args.get('date_filter')
    visitor_type_filter = request.args.get('visitor_type_filter')

    total_visitors = Visitor.query.count()
    today = datetime.today().date()
    visitors_today = Visitor.query.filter_by(date=today).count()
    last_visitor = Visitor.query.order_by(Visitor.id.desc()).first()
    last_registration = (
        f"{last_visitor.name} {last_visitor.surname} {last_visitor.date.strftime('%Y-%m-%d')} - {last_visitor.time.strftime('%H:%M:%S')}"
        if last_visitor else "Artık günlükçü yok"
    )

    ####Dinamik sorgu oluşturma (yeni uygulama)
    visitors_query = Visitor.query

    if query:
        visitors_query = visitors_query.filter(
            or_(
                func.lower(Visitor.name).contains(query.lower()),
                func.lower(Visitor.surname).contains(query.lower()),
                Visitor.phone.contains(query)
            )
        )

    if date_filter:
        visitors_query = visitors_query.filter(Visitor.date == date_filter)

    if visitor_type_filter:
        visitors_query = visitors_query.filter(Visitor.visitor_type == visitor_type_filter)

    visitors = visitors_query.order_by(Visitor.date.desc(), Visitor.time.desc()).all()

    return render_template(
        'dashboard.html',
        visitors=visitors,
        total_visitors=total_visitors,
        visitors_today=visitors_today,
        last_registration=last_registration
    )

@app.route("/register_visitor")
def register_visitor():
    return render_template("registervisitor.html")

@app.route('/visitor_info/<int:id>')
@login_required
def visitor_info(id):
    visitor = Visitor.query.get_or_404(id)
    return render_template('visitor_info.html', visitor=visitor)


@app.route('/editvisitor/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_visitor(id):
    visitor = Visitor.query.get_or_404(id)
    if request.method == 'POST':
        visitor.name = request.form.get('name')
        visitor.surname = request.form.get('surname')
        visitor.phone = request.form.get('phone')
        visitor.visitor_type = request.form["visitor_type"] ####Yeni alan: Ziyaretçi türünü güncellemek ve veritabanına kaydetmek için
        
        db.session.commit()
        flash("Ziyaretçi bilgileri güncellendi!", "success")
        ###return redirect(url_for('dashboard'))
        return redirect(url_for('visitor_info', id=visitor.id))  ###Değişiklikleri kontrol etmek için ayrıntılar sayfasına yönlendirin (yeni)

    return render_template('editvisitor.html', visitor=visitor)

@app.route('/deletevisitor/<int:id>', methods=['POST'])
@login_required
def delete_visitor(id):
    visitor = Visitor.query.get_or_404(id)
    db.session.delete(visitor)
    db.session.commit()

    delete_visitor_from_json(id)  # visitors.json dosyasından da sil

    flash("Ziyaretçi başarıyla silindi!", "danger")
    return redirect(url_for('dashboard'))


# Kullanıcıların şifrelerini kurtarmalarına olanak sağlayan "Şifremi Unuttum" sayfasına giden yol.
@app.route("/forgot-password", methods=["GET", "POST"]) 
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        # Burada kurtarma bağlantısını gönderme mantığını uygularsınız
        flash("Şifre sıfırlama bağlantısı e-postanıza gönderildi!", "success")
        return redirect(url_for("login"))
    return render_template("forgot-password.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Kullanıcıyı çıkış yap
    flash("Başarıyla çıkış yaptınız!", "info")  # Kullanıcıya mesaj göster
    return redirect(url_for('index'))  # Giriş sayfasına yönlendir

####yeni uygulama (CSV ve PDF yazdırmak için)
@app.route('/export_csv')
@login_required
def export_csv():
    visitors = Visitor.query.all()

    def generate_csv():
        yield "Id,Ad,Soyad,Telefon,Tarih,Saat\n"
        for v in visitors:
            yield f"{v.id},{v.name},{v.surname},{v.phone},{v.date},{v.time.strftime('%H:%M:%S')}\n"
    return Response(generate_csv(), mimetype='text/csv', headers={"Content-Disposition": "attachment; filename=visitors.csv"})


@app.route('/export_pdf')
@login_required
def export_pdf():
    visitors = Visitor.query.all()
    
    #PDF'yi başlat
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    #Arial yazı tipini kullan
    pdf.add_font('Arial', '', 'static/fonts/arial.ttf', uni=True)
    pdf.set_font('Arial', '', 10)

    #Belge başlığı
    pdf.cell(190, 10, "Ziyaretçi Listesi", ln=True, align="C")
    pdf.ln(10)  # Başlıktan sonra boşluk

    #Tablo başlığı
    pdf.set_font("Arial", "B", 10)
    pdf.cell(30, 10, "ID", border=1)
    pdf.cell(50, 10, "Ad", border=1)
    pdf.cell(50, 10, "Soyad", border=1)
    pdf.cell(40, 10, "Telefon", border=1)
    pdf.cell(30, 10, "Tarih", border=1)
    pdf.cell(30, 10, "Saat", border=1)
    pdf.ln(10)

    #Ziyaretçi verilerini ekle
    pdf.set_font("Arial", "", 10)
    for v in visitors:
        pdf.cell(30, 10, str(v.id), border=1)
        pdf.cell(50, 10, v.name, border=1)
        pdf.cell(50, 10, v.surname, border=1)
        pdf.cell(40, 10, v.phone, border=1)
        pdf.cell(30, 10, str(v.date), border=1)
        pdf.cell(30, 10, v.time.strftime('%H:%M:%S'), border=1)
        pdf.ln(10)  # Her ziyaretçiden sonra yeni satır
    #Hataları önlemek için PDF'yi UTF-8 kodlamasıyla dışa aktarın
    return Response(pdf.output(dest='S').encode('latin1'), mimetype="application/pdf", headers={"Content-Disposition": "attachment; filename=visitors.pdf"})

####yeni uygulama
@app.route('/statistics', methods=['GET'])
@login_required
def statistics():
    today = datetime.today().date()
    start_week = today - timedelta(days=today.weekday())
    start_month = today.replace(day=1)

    total_month = Visitor.query.filter(Visitor.date >= start_month).count()

    selected_month = request.args.get('month')
    if selected_month:
        start_selected_month = datetime.strptime(selected_month, '%Y-%m')
        end_selected_month = start_selected_month + timedelta(days=30)
        total_selected_month = Visitor.query.filter(
            Visitor.date >= start_selected_month,
            Visitor.date < end_selected_month
        ).count()
    else:
        total_selected_month = total_month

    total_today = Visitor.query.filter(Visitor.date == today).count()
    total_week = Visitor.query.filter(Visitor.date >= start_week).count()
    total_month = Visitor.query.filter(Visitor.date >= start_month).count()

    top_visitors = (
        db.session.query(Visitor.name, Visitor.surname, Visitor.phone, func.count(Visitor.phone).label('total'))
        .group_by(Visitor.name, Visitor.surname, Visitor.phone)
        .order_by(func.count(Visitor.phone).desc())
        .limit(5)
        .all()
    )

    visits_by_month = (
        db.session.query(func.strftime('%Y-%m', Visitor.date).label('month'), func.count().label('total'))
        .group_by('month')
        .order_by('month')
        .all()
    )

    return render_template("statistics.html",
                           total_today=total_today,
                           total_week=total_week,
                           total_month=total_month,
                           total_selected_month=total_selected_month,
                           selected_month=selected_month,
                           top_visitors=top_visitors,
                           visits_by_month=visits_by_month)



# Uygulamayı çalıştırma
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
