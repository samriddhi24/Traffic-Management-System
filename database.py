import sqlite3
import os
from datetime import datetime
from config import SNAPSHOT_DIR

# Ensure snapshot directory exists
os.makedirs(SNAPSHOT_DIR, exist_ok=True)

# Connect to database
conn = sqlite3.connect("traffic_violations.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS violations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number_plate TEXT,
        violation TEXT,
        image_path TEXT,
        location TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

def store_violation(number_plate, violation, image_path=None, location=None):
    try:
        cursor.execute(
            "INSERT INTO violations (number_plate, violation, image_path, location) VALUES (?, ?, ?, ?)",
            (number_plate, violation, image_path, location)
        )
        conn.commit()
    except Exception as e:
        print(f"[DB ERROR] {e}")

def close_connection():
    conn.close()