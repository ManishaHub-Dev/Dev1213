import shutil

def backup_db():
    shutil.copy('example.db', 'example_backup.db')
    print("Database backup created.")

if __name__ == "__main__":
    backup_db()