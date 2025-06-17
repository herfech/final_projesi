# Konut Ziyaretçi Kayıt Sistemi  

Bu proje, konut ziyaretçilerini kayıt altına almak ve yönetmek için geliştirilen bir **web uygulamasıdır**.  
Kullanıcı dostu arayüzü ile **ziyaretçileri ekleme, görüntüleme, düzenleme ve yönetme** işlemleri kolaylaştırılmıştır.

---

## 📌 Yeni Özellikler & Güncellemeler  

✅ **Ziyaretçi türüne göre kontrol** → Artık erişim ve kayıt işlemleri ziyaretçi türüne bağlı.  
✅ **Ziyaretçi detay sayfasında tür bilgisi** → Ziyaretçinin kategorisi artık açıkça görülebiliyor.  
✅ **Ziyaretçi türü düzenleme & soyadı değiştirme** → Düzenleme ekranında artık ziyaretçi türü değiştirilebilir.  
✅ **Renk farklılaştırma** → Ziyaretçiler renk kodları ile ayrıldı, yönetim daha kolay!  
✅ **Dinamik panel** → Hızlı filtreler (tarih & ziyaretçi türü) ile daha esnek yönetim.  
✅ **Ziyaretçi listesi dışa aktarma** → CSV & PDF formatında indirme seçenekleri eklendi.  
✅ **Yeni istatistikler sayfası** → Ziyaretçi verileri artık ay bazında filtrelenebilir.  
✅ **Arama geliştirmeleri** → Ziyaretçileri artık **telefon numarasına göre** arayabilirsiniz.  
✅ **Ana sayfa arka planı güncellendi** → Daha modern ve akıcı bir görünüm sağlandı.  

---

## 📌 zellikler 

✅ Modern ve responsive tasarım
✅ Flask framework kullanımı
✅ Bootstrap 5 entegrasyonu
✅ Kullanıcı dostu arayüz
✅ Ziyaretçi kaydı ve yönetimi
✅ Şifremi Unuttum özelliği
✅ Arama ve filtreleme sistemi
✅ Flask ile temiz ve düzenli kod
✅ Veri yedekleme ve dışa aktarma sistemi

---

## 📄 Sayfalar ve İşlevleri  

### 🌐 Ana Sayfa (`index.html`)  
- Uygulamanın kısa tanıtımı ve giriş seçenekleri  

### 🔐 Giriş (`login.html`) 
- Kullanıcı giriş formu  
- Şifre kurtarma bağlantısı  

### ✍ Ziyaretçi Kaydı (`registervisitor.html`) 
- Ziyaretçi türü, ad, soyad, telefon ve ziyaret tarihi bilgilerini kaydetme  

### 📊 Panel (`dashboard.html`)
- **Filtreleme sistemleri** (Tarih & ziyaretçi türü)  
- **Renk kodlu ziyaretçi listesi**  
- **Veri dışa aktarma** seçenekleri (CSV, PDF)  

### 📈 İstatistikler (`statistics.html`) 
- **Ziyaretçi verilerinin aylık analizi**  
- **Interaktif grafikler ve filtreleme seçenekleri** 

### 📝 **Düzenleme & Detay (`editvisitor.html` & `visitor_info.html`)**  
- Ziyaretçi bilgilerinin güncellenmesi  
- Ziyaretçi türünü değiştirme ve soyadı düzenleme  

---

### 🔑 Şifre Kurtarma (`forgot-password.html`) 
- Kullanıcıların şifrelerini sıfırlaması için bağlantı oluşturur  
- Kurtarma bağlantısı ekrana yazdırılır  

---

## 🛠 Kullanılan Teknolojiler 

✅ **Backend:** Python (Flask, Flask-Migrate, Flask-SQLAlchemy)  
✅ **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (Chart.js)  
✅ **Veritabanı:** SQLite (Flask-Migrate ile yönetim)  
✅ **Dosya Yönetimi:** Zipfile, CSV & PDF dışa aktarma  

---

## 🚀 **Kurulum ve Çalıştırma**  

        ```bash
        # 1️⃣ Depoyu klonlayın:
        git clone https://github.com/kullaniciadi/final_projesi.git
        cd final_projesi

        # 2️⃣ Gerekli paketleri yükleyin:
        pip install -r requirements.txt

        # 3️⃣ Veritabanını oluşturun:
        flask db upgrade

        # 4️⃣ Uygulamayı başlatın:
        python app.py
```

5️⃣ **Tarayıcıdan açın:**  
📌 [http://localhost:5000](http://localhost:5000)  

---

## 📂 **Proje Yapısı**  

```bash
Final_hafta/
├── templates/                  # HTML şablonları
│   ├── base.html               # Ana şablon dosyası
│   ├── index.html              # Ana sayfa
│   ├── login.html              # Kullanıcı giriş sayfası
│   ├── registervisitor.html    # Ziyaretçi kaydı
│   ├── dashboard.html          # Yönetim paneli
│   ├── editvisitor.htm         # Ziyaretçi düzenleme sayfası
│   ├── visitor_info.html       # Ziyaretçi detay sayfası
│   ├── statistics.html           # İstatistik sayfası
│   ├── createaccount.html      # Kullanıcı hesabı oluşturma sayfası
│   ├── forgot-password.html    # Şifre kurtarma
├── static/                  # CSS ve görseller
│   ├── styles.css           # Stiller
│   ├── img/                 # Görseller
│   ├── fonts                # yazı tipleri
├── instance/                # Veritabanı dosyası
│   ├── site.db              # SQLite veritabanı
├── migrations/
│   ├── versions/            # Veritabanına uygulanan geçiş dosyaları  
│   ├── pycache__/           # Python tarafından oluşturulan önbellek dosyaları  
│   ├── alembic.ini          # Alembic yapılandırma dosyası  
│   ├──env.py                # Geçiş ortamı yapılandırmasını yönetir  
│   ├──README                # Geçiş sistemiyle ilgili dokümantasyon dosyası  
│   ├──script.py.mako        # Geçiş dosyalarını oluşturmak için kullanılan şablon
├── app.py                   # Ana uygulama dosyası
├── models.py                # Veritabanı modelleri
├── data_manager.py          # JSON ve veritabanı işlemleri
├── export_data.py           # SQLite verilerini JSON’a dönüştüren ve ZIP arşivi 
├── manager.py               # Flask komut satırı yönetimi ve veritabanı işlemleri
├── users.json               # Kullanıcı bilgileri
├── visitors.json            # Ziyaretçi bilgileri
├── requirements.txt         # Gerekli Python paketleri listesi
├── README.md                # Proje açıklamaları
├── backup.zip               # Ziyaretçi ve kullanıcı verilerini içeren sıkıştırılmış dosya
```

---

## 🔄 Veri Yedekleme ve Dışa Aktarma  

📌 Veri yedekleme sistemi, `export_data.py` dosyasıyla çalışır.  

✅ Veritabanındaki `visitor` ve `user` tablolarını okur.**  
✅ JSON formatında dosya oluşturur (`users.json`, `visitors.json`).  
✅ Tüm verileri `backup.zip` içine sıkıştırır. 

### ✨ Çalıştırma Komutu:  
```bash
python export_data.py
```
📌 **Bu komut, verileri güncelleyerek `backup.zip` dosyasını oluşturur.**  

---

## 🎨 Tasarım Özellikleri

### 🔹 Tasarım Güncellemeleri 

✅ **Yeni arka plan tasarımı** → Ana sayfa görsel olarak daha şık hale getirildi.  
✅ **Renk kodlu ziyaretçi listesi** → Görsel farklılaştırma sayesinde yönetim daha kolay.  
✅ **Mobil uyumluluk geliştirmeleri** → Bootstrap ile tam ekran uyumu sağlandı.

### 🔹 Renkler  
- Primary: Mavi (#0d6efd)  
- Success: Yeşil (#198754)  
- Warning: Sarı (#ffc107)  

### 🔹 Kartlar ve Arayüz 
✅ Gölgeli tasarım (shadow) 
✅ Hover efektleri  
✅ Bootstrap ikon entegrasyonu 

---
📌 **Render sitesinin bağlantısı:**  
👉 **[https://ziyaretci-kayit.onrender.com](https://ziyaretci-kayit.onrender.com)**  

---
