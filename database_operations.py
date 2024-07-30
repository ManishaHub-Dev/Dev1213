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

import sqlite3
import unittest

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    
    def tearDown(self):
        self.conn.close()
    
    def test_insert_user(self):
        self.c.execute("INSERT INTO users (name, age) VALUES ('Drey', 28)")
        self.c.execute("SELECT * FROM users WHERE name='Drey'")
        user = self.c.fetchone()
        self.assertEqual(user[1], 'Drey')
        self.assertEqual(user[2], 28)

if __name__ == '__main__':
    unittest.main()