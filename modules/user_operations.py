import logging
from database import get_connection

def add_user(name, age, email):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        logging.info(f"Inserted user {name}")
        conn.commit()