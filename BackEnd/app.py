from flask import Flask, request, jsonify, redirect, url_for, session
from flask_cors import CORS
from user import User

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

user = User()

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get("email")
    plain_password = request.json.get("plain_password")

    # calling the login function from user.py
    res = user.loginAccount(email, plain_password)
    if res == "successful":
        return jsonify({"message": "Successfully logged in"}), 201
    else:
        return jsonify({"error": res}), 409

@app.route('/register', methods=['POST'])
def register():
    fullName = request.json.get("fullName")
    email = request.json.get("email")
    plain_password = request.json.get("plain_password")
    address = request.json.get("address")
    usertype = request.json.get("usertype")

    # calling the register function from user.py
    res = user.createAccount(fullName, email, plain_password, address, usertype)
    if res == "successful":
        return jsonify({"message": "Successfully registered"}), 201
    else:
        return jsonify({"error": res}), 409

if __name__ == '__main__':
    app.run(debug=True)