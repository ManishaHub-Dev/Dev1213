import hashlib

users = {}

def register(username, password):
    if username in users:
        return "User already exists!"
    users[username] = hashlib.sha256(password.encode()).hexdigest()
    return "User registered successfully!"

def login(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == hashed:
        return "Login successful!"
    else:
        return "Login failed!"