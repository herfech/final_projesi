# Ziyaretçi Kayıt Sistemi  

Bu proje, ziyaretçi kayıtlarını yönetmek için geliştirilen bir web uygulamasıdır.  
Kullanıcı dostu bir arayüzle, ziyaretçi bilgilerini kaydetme, görüntüleme ve düzenleme işlemlerini kolaylaştırır.  

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
- Tanıtım ve giriş butonu  
- Uygulamaya genel bakış  

### 🔐 Giriş (`login.html`) 
- Kullanıcı giriş formu  
- Şifre kurtarma bağlantısı  

### ✍ Ziyaretçi Kaydı (`registervisitor.html`) 
- Ad, soyad, telefon ve ziyaret tarihi bilgileri  
- Kaydetme ve doğrulama işlemleri  

### 📊 Panel (`dashboard.html`)
- İstatistik kartları  
- Ziyaretçi listesi ve işlem butonları  
- Verileri düzenleme ve silme özellikleri  

### 🔑 Şifre Kurtarma (`forgot-password.html`) 
- Kullanıcıların şifrelerini sıfırlaması için bağlantı oluşturur  
- Kurtarma bağlantısı ekrana yazdırılır  

---

## 🛠 Kullanılan Teknolojiler 

- Python (Flask) → Backend geliştirme  
- HTML5 → Sayfa yapısı  
- CSS3 → Görsel tasarım  
- Bootstrap 5 → Responsive arayüz  
- inja2 → Template engine  
- SQLite → Veritabanı yönetimi  
- Flask-Mail → Şifre kurtarma işlemleri  
- Zipfile → Veri yedekleme ve arşivleme  

---

## 🚀 **Kurulum ve Çalıştırma**  

        1️⃣ Depoyu klonlayın:  
        ```bash
        git clone https://github.com/kullaniciadi/final_projesi.git
        cd final_projesi
        ```

        2️⃣ Gerekli paketleri yükleyin:  
        ```bash
        pip install -r requirements.txt
        ```

        3️⃣ Veritabanını oluşturun: 
        ```bash
        python -c "from app import db; db.create_all()"
        ```

        4️⃣ Uygulamayı başlatın:
        ```bash
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
│   ├── createaccount.html      # Kullanıcı hesabı oluşturma sayfası
│   ├── forgot-password.html    # Şifre kurtarma
├── static/                  # CSS ve görseller
│   ├── styles.css           # Stiller
│   ├── img/                 # Görseller
├── instance/                # Veritabanı dosyası
│   ├── site.db              # SQLite veritabanı
├── app.py                   # Ana uygulama dosyası
├── models.py                # Veritabanı modelleri
├── data_manager.py          # JSON ve veritabanı işlemleri
├── export_data.py           # SQLite verilerini JSON’a dönüştüren ve ZIP arşivi oluşturan betik
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

### 🔹 Renkler  
- Primary: Mavi (#0d6efd)  
- Success: Yeşil (#198754)  
- Warning: Sarı (#ffc107)  

### 🔹 Responsive Tasarım  
✅ Mobil, tablet ve masaüstü uyumlu 
✅ Bootstrap grid sistemi ile esnek yerleşim 

### 🔹 Kartlar ve Arayüz 
✅ Gölgeli tasarım (shadow) 
✅ Hover efektleri  
✅ Bootstrap ikon entegrasyonu 

---
