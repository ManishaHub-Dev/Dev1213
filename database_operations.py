import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to create the database and tables
def initialize_database():
    # Connect to the database (or create it)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Create the 'users' table with username and password fields
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    logging.info("Created table 'users'")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    logging.info("Database initialized successfully.")

# Main execution
if __name__ == "__main__":
    initialize_database()
    print("Database operations completed successfully.")