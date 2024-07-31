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

    # Create the 'profiles' table with a foreign key to the 'users' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            bio TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    logging.info("Created table 'profiles'")

    # Create the 'roles' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY,
            role_name TEXT UNIQUE NOT NULL
        )
    ''')
    logging.info("Created table 'roles'")

    # Create the 'user_roles' table to associate users with roles
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_roles (
            user_id INTEGER NOT NULL,
            role_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (role_id) REFERENCES roles (id),
            PRIMARY KEY (user_id, role_id)
        )
    ''')
    logging.info("Created table 'user_roles'")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    logging.info("Database initialized successfully.")

# Main execution
if __name__ == "__main__":
    initialize_database()
    print("Database operations completed successfully.")
