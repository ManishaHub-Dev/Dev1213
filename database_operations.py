import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to the database (or create it)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
logging.info("Created table 'users'")

# Insert some records
c.execute("INSERT INTO users (name, age) VALUES ('Drey', 28)")
c.execute("INSERT INTO users (name, age) VALUES ('Allison', 31)")
logging.info("Inserted records into 'users'")

# Complex query
c.execute("SELECT AVG(age) FROM users")
avg_age = c.fetchone()[0]
logging.info(f"Average age of users: {avg_age}")

# Commit the changes and close the connection
conn.commit()
conn.close()

logging.info("Database operations completed successfully.")

