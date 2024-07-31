import sqlite3
import unittest

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)''')

    def tearDown(self):
        self.conn.close()

    def test_insert_user(self):
        self.c.execute("INSERT INTO users (name, age, email) VALUES ('Alice', 30, 'alice@example.com')")
        self.c.execute("SELECT * FROM users WHERE name='Alice'")
        user = self.c.fetchone()
        self.assertEqual(user[1], 'Alice')
        self.assertEqual(user[2], 30)
        self.assertEqual(user[3], 'alice@example.com')

    def test_backup(self):
        # Mock backup test if applicable
        pass

if __name__ == '__main__':
    unittest.main()
