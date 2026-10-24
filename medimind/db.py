import sqlite3
from datetime import datetime, timezone
from .config import DB_PATH

def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS chat_logs(
        id INTEGER PRIMARY KEY, created_at TEXT, user_message TEXT,
        intent TEXT, confidence REAL)""")

def save_chat(message, intent, confidence):
    # Prototype logging: stores message text locally. Do not enter personal health data.
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT INTO chat_logs(created_at,user_message,intent,confidence) VALUES(?,?,?,?)",
        (datetime.now(timezone.utc).isoformat(), message[:1200], intent, float(confidence)))

def log_summary():
    with sqlite3.connect(DB_PATH) as c:
        row = c.execute("SELECT COUNT(*), AVG(confidence) FROM chat_logs").fetchone()
    return {"saved_messages": int(row[0] or 0), "mean_model_confidence": round(float(row[1]), 3) if row[1] is not None else None,
            "note": "Local development logs only; confidence is not medical certainty."}
