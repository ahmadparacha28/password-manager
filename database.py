import sqlite3

def connect():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords(
            id INTEGER PRIMARY KEY,
            website TEXT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_data(website, username, password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                   (website, username, password))
    conn.commit()
    conn.close()

def view_data():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords")
    rows = cursor.fetchall()
    conn.close()
    return rows