import shutil

def backup_database(db_file):
    backup_file = f"{db_file}.bak"
    shutil.copy(db_file, backup_file)
    print(f"Backup created: {backup_file}")