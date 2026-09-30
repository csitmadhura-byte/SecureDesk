import sqlite3
import os
from datetime import datetime


DATABASE_FOLDER = "logs"
DATABASE_FILE = os.path.join(DATABASE_FOLDER, "securedesk.db")


def create_database():
    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_type TEXT NOT NULL,
            status TEXT NOT NULL,
            details TEXT,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_scan(scan_type, status, details):
    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO scan_history
        (scan_type, status, details, timestamp)
        VALUES (?, ?, ?, ?)
    """, (
        scan_type,
        status,
        details,
        timestamp
    ))

    connection.commit()
    connection.close()


def get_scan_history(limit=10):
    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, scan_type, status, details, timestamp
        FROM scan_history
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    records = cursor.fetchall()

    connection.close()

    return records