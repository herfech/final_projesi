
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

## 🚀 Kurulum ve Çalıştırma  

1. Depoyu klonlayın:  
```bash
git clone https://github.com/kullaniciadi/ziyaretci-kayit-sistemi.git
cd ziyaretci-kayit-sistemi
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
│   ├── forgot-password.html
│   ├── createaccount.html
│   ├── dashboard.html
│   ├── visitor_info.html
│   ├── editvisitor.html
├── static/
│   ├── styles.css
│   ├── img/
├── instance/
│   ├── site.db
├── app.py
├── data_manager.py
├── models.py
├── users.json
├── visitors.json
├── requirements.txt
├── README.md
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

Render sitesinin bağlantısı
https://ziyaretci-kayit.onrender.com
