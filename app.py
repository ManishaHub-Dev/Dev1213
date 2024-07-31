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

if __name__ == '__main__':
    app.run(debug=True)