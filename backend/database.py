import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "activity_log.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_name TEXT NOT NULL,
            window_title TEXT,
            start_time TEXT NOT NULL,
            end_time TEXT
        )
    """)
    conn.commit()
    conn.close()
