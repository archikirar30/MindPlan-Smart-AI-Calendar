import time
import datetime
import win32gui
import win32process
import psutil
from backend.models.activity_model import log_activity
from backend.database import init_db

# Ensure DB & tables exist before tracking
init_db()

def get_active_window():
    """Get the currently active window's app name and title (Windows)."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        app_name = process.name()
        window_title = win32gui.GetWindowText(hwnd)
        return app_name, window_title
    except Exception:
        return None, None

def track_activity(interval: int = 10):
    """Track usage duration of active apps and log to DB."""
    last_app = None
    last_title = None
    start_time = None

    while True:
        app, title = get_active_window()
        if app and (app != last_app or title != last_title):
            # Log the previous app if it exists
            if last_app:
                end_time = datetime.datetime.now().isoformat()
                log_activity(last_app, last_title, start_time, end_time)

            # Reset tracker for the new active app
            last_app, last_title = app, title
            start_time = datetime.datetime.now().isoformat()

        time.sleep(interval)
