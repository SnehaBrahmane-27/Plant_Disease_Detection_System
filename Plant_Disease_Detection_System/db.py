import sqlite3
from datetime import datetime
import os



def create_tables():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 username TEXT PRIMARY KEY,
                 password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT,
                 image_path TEXT,
                 predicted_disease TEXT,
                 timestamp TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validate_login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def save_prediction(username, image_path, predicted_disease):
    abs_path = os.path.abspath(image_path)  # Convert to full path
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO predictions (username, image_path, predicted_disease, timestamp) VALUES (?, ?, ?, ?)", 
              (username, abs_path, predicted_disease, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_user_history(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM predictions WHERE username=?", (username,))
    data = c.fetchall()
    conn.close()
    return data

def delete_prediction(prediction_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM predictions WHERE id=?", (prediction_id,))
    conn.commit()
    conn.close()
