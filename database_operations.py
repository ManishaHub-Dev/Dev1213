import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert some records
c.execute("INSERT INTO users (name, age) VALUES ('Drey', 28)")
c.execute("INSERT INTO users (name, age) VALUES ('Allison', 31)")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database operations completed successfully.")
