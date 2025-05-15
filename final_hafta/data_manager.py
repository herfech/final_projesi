
import json
from models import User, db

JSON_FILE = "users.json"

def load_users():
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

        

VISITORS_JSON_FILE = "visitors.json"

def load_visitors():
    try:
        with open(VISITORS_JSON_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_visitors(new_visitor):
    visitors = load_visitors()
    
    visitors.append({
        "id": new_visitor.id,
        "name": new_visitor.name,
        "surname": new_visitor.surname,
        "phone": new_visitor.phone,
        "date": str(new_visitor.date),
        "time": str(new_visitor.time)
    })
    
    with open(VISITORS_JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(visitors, file, ensure_ascii=False, indent=4)



def delete_visitor_from_json(visitor_id, file_path='visitors.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            visitors = json.load(f)
        visitors = [v for v in visitors if v['id'] != visitor_id]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(visitors, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("JSON'dan silme hatası:", e)
        return False




