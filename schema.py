# db configs


import sqlite3

DB_PATH = "users.db"




def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Still insecure, but now safe to re-run
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

    cursor.execute("INSERT INTO users VALUES ('admin','admin123')")

    conn.commit()
