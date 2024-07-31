import sqlite3

def migrate():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Example migration: Adding a new column
    c.execute('ALTER TABLE users ADD COLUMN email TEXT')
    
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    migrate()