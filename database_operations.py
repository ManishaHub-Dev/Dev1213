import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get the database URL from environment variables
database_url = os.getenv('DATABASE_URL', 'example.db')  # Default to 'example.db' if not set

def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)''')
    logging.info("Created table 'users'")
    conn.commit()
    conn.close()

def add_user(name, age, email):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    logging.info(f"Inserted user {name}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    add_user('Drey', 28, 'charlie@example.com')
    # More user operations can be added here

