from backend.database import get_connection

def log_activity(app_name: str, window_title: str, start_time: str, end_time: str = None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO activities (app_name, window_title, start_time, end_time)
        VALUES (?, ?, ?, ?)
    """, (app_name, window_title, start_time, end_time))
    conn.commit()
    conn.close()

def get_all_activities():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities ORDER BY start_time DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

