import hashlib
import logging

# Configure logging
logging.basicConfig(
    filename='authentication.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Updated users dictionary to store both password and role
users = {}

# Updated register function to include role
def register(username, password, role):
    if username in users:
        logging.warning(f"Registration attempt failed: User '{username}' already exists.")
        return "User already exists!"
    
    # Store password and role in the dictionary
    users[username] = {
        'password': hashlib.sha256(password.encode()).hexdigest(),
        'role': role
    }
    logging.info(f"User '{username}' with role '{role}' registered successfully.")
    return "User registered successfully!"

def login(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username]['password'] == hashed:
        logging.info(f"User '{username}' with role '{users[username]['role']}' logged in successfully.")
        return "Login successful!"
    else:
        logging.warning(f"Failed login attempt for user '{username}'.")
        return "Login failed!"
