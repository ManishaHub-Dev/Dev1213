import logging
from database import create_table
from user_operations import add_user

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    create_table()
    add_user('Charlie', 28, 'charlie@example.com')

if __name__ == "__main__":
    main()