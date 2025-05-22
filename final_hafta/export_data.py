import json
import sqlite3
import zipfile
import os

# Veritabanından JSON'a veri aktarma ve ZIP oluşturma işlevi
def export_data():
    try:
        conn = sqlite3.connect("instance/site.db")

        cursor = conn.cursor()

        # Ziyaretçileri dışa aktar
        cursor.execute("SELECT * FROM visitor")
        visitors = cursor.fetchall()
        visitor_columns = [column[0] for column in cursor.description]
        visitor_list = [dict(zip(visitor_columns, row)) for row in visitors]

        with open("visitors.json", "w", encoding="utf-8") as v_file:
            json.dump(visitor_list if visitors else [], v_file, ensure_ascii=False, indent=4)

        print("visitors.json dosyası başarıyla oluşturuldu.")

        # Kullanıcıları dışa aktar
        cursor.execute("SELECT * FROM user")
        users = cursor.fetchall()
        user_columns = [column[0] for column in cursor.description]
        user_list = [dict(zip(user_columns, row)) for row in users]

        with open("users.json", "w", encoding="utf-8") as u_file:
            json.dump(user_list if users else [], u_file, ensure_ascii=False, indent=4)

        print("users.json dosyası başarıyla oluşturuldu.")

        conn.close()
        print("Veriler JSON'a başarıyla aktarıldı.")

        # SIKIŞTIRMADAN ÖNCE DOSYA KONTROLÜNÜ ZORLA
        if os.path.exists("visitors.json") and os.path.exists("users.json"):
            print("JSON dosyaları mevcuttur. Sıkıştırmaya devam ediliyor...")
            with zipfile.ZipFile("backup.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
                zipf.write("visitors.json", arcname="visitors.json")
                zipf.write("users.json", arcname="users.json")
            print("Sıkıştırılmış dosya backup.zip başarıyla oluşturuldu!")
        else:
            print("Hata: Sıkıştırılacak JSON dosyası bulunamadı.")

    except Exception as e:
        print(f"Dışa aktarma sırasında hata: {e}")

# Dışa aktarmayı çalıştır
if __name__ == "__main__":
    export_data()