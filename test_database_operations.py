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