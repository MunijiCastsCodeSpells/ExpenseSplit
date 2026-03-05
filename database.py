import sqlite3


def init_db():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        payer TEXT,
        amount REAL,
        category TEXT,
        shares TEXT
    )
    """)

    conn.commit()
    conn.close()