# database.py

import sqlite3
import logging
import os

# Get the database URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL', 'example.db')

def get_connection():
    return sqlite3.connect(DATABASE_URL)

def create_table():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)''')
        logging.info("Created table 'users'")
        conn.commit()
