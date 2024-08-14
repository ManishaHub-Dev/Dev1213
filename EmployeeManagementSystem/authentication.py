import hashlib
import logging

# Configure logging
logging.basicConfig(
    filename='authentication.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

users = {}

def register(username, password):
    if username in users:
        logging.warning(f"Registration attempt failed: User '{username}' already exists.")
        return "User already exists!"
    users[username] = hashlib.sha256(password.encode()).hexdigest()
    logging.info(f"User '{username}' registered successfully.")
    return "User registered successfully!"

def login(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == hashed:
        logging.info(f"User '{username}' logged in successfully.")
        return "Login successful!"
    else:
        logging.warning(f"Failed login attempt for user '{username}'.")
        return "Login failed!"