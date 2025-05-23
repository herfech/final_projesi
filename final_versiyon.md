# Ziyaretçi Kayıt Sistemi

Bu proje, ziyaretçi kayıtlarını yönetmek için geliştirilen bir web uygulamasıdır.  
Kullanıcı dostu bir arayüzle, ziyaretçi bilgilerini kaydetme, görüntüleme ve düzenleme işlemlerini kolaylaştırır.

## 📌 Özellikler  

✅ Modern ve responsive tasarım  
✅ Flask framework kullanımı  
✅ Bootstrap 5 entegrasyonu  
✅ Kullanıcı dostu arayüz  
✅ Ziyaretçi kaydı ve yönetimi  
✅ Şifremi Unuttum özelliği  
✅ Arama ve filtreleme sistemi  
✅ Flask ile temiz ve düzenli kod  

## 📄 Sayfalar  

### 🌐 **Ana Sayfa (index.html)**  
- Tanıtım ve giriş butonu  

### 🔐 **Giriş (login.html)**  
- Kullanıcı girişi formu  
- Şifre kurtarma bağlantısı  

### ✍ **Ziyaretçi Kaydı (registervisitor.html)**  
- Ad, soyad, telefon ve ziyaret tarih bilgileri  
- Kaydet butonu  

### 📊 **Panel (dashboard.html)**  
- İstatistik kartları  
- Ziyaretçi listesi ve işlem butonları  

## 🛠 Kullanılan Teknolojiler  

- Python (Flask)  
- HTML5  
- CSS3  
- Bootstrap 5  
- Jinja2 Template Engine
- SQLite (Veritabanı)
- Flask-Maıl (Şifre kurtarma için)
- Zipfile (Veri yedekleme için)

## 🚀 Kurulum ve Çalıştırma  

1. Depoyu klonlayın:  
```bash
git clone https://github.com/kullaniciadi/final_projesi.git
cd final_projesi
```

2. Gerekli paketleri yükleyin:  
```bash
pip install -r requirements.txt
```

3. Uygulamayı başlatın:  
```bash
python app.py
```

4. Tarayıcıda [http://localhost:5000](http://localhost:5000) adresine gidin.

## 📂 Proje Yapısı  

```bash
Final_hafta/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── registervisitor.html
│   ├── dashboard.html
│   ├── editvisitor.htm
│   ├── visitor_info.html
│   ├── createaccount.html
│   ├── forgot-password.html
├── static/
│   ├── styles.css
│   ├── img/
├── instance/
│   ├── site.db           # SQLite veritabanı dosyası
├── app.py                # Ana uygulama dosyası
├── models.py             # Veritabanı modelleri
├── data_manager.py       # JSON ve veritabanı işlemleri
├── export_data.py        # SQLite verilerini JSON’a dönüştüren ve ZIP arşivi oluşturan betik
├── users.json            # Kullanıcı bilgilerini saklayan JSON dosyası
├── visitors.json         # Ziyaretçi kayıtlarını saklayan JSON dosyası
├── requirements.txt      # Gerekli paketler listes
├── README.md             # Proje bilgileri
├── backup.zip            # Ziyaretçi ve kullanıcı verilerini içeren sıkıştırılmış dosya
```

## 🎨 Tasarım Özellikleri  

### 🔹 Renkler  
- *Primary*: Mavi (#0d6efd)  
- *Success*: Yeşil (#198754)  
- *Warning*: Sarı (#ffc107)  

### 🔹 Responsive Tasarım  
- Mobil, tablet ve masaüstü uyumlu  
- Bootstrap grid sistemi ile esnek yerleşim  

### 🔹 Kartlar ve Arayüz  
- Gölgeli tasarım (shadow)  
- Hover efektleri  
- Bootstrap ikon entegrasyonu  
