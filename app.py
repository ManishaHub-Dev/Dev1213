from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    create_user(username, password)
    return jsonify({"message": "User created successfully"}), 201

@app.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if authenticate_user(username, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
        
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return jsonify(users), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (id,))
    user = c.fetchone()
    conn.close()
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    username = data['username']
    password = hash_password(data['password'])
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("UPDATE users SET username=?, password=? WHERE id=?", (username, password, id))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated successfully"}), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)