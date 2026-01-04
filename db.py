import sqlite3

def get_db():
    return sqlite3.connect("users.db")  # 🚨 hard-coded path
