# Much help from: https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/

from flask import Flask, request, jsonify, session, g
from flask_cors import CORS
from user import User
from functools import wraps
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

app.secret_key = 'canputanythinghere'
user = User()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return jsonify({"error": "Log in first!"}), 401
        return f(*args, **kwargs)
    return decorated_function


@app.before_request
def load_user():
    g.email = None
    if 'email' in session:
        g.email = session['email']
        cursor = sqlite3.connect("StoreDatabase.db").cursor()
        cursor.execute("SELECT AccountID, FullName, Email, Password, Address, UserType FROM UserAccounts WHERE Email=?", (g.email,))
        user_details = cursor.fetchone()
        if user_details:
            g.accountId = user_details[0]
            g.fullName = user_details[1]
            g.password = user_details[3]
            g.address = user_details[4]
            g.usertype = user_details[5]
        else:
            g.accountId = None
            g.fullName = None
            g.address = None
            g.usertype = None


@app.route('/dashboard')
@login_required
def dashboard():
    if g.email:
        return jsonify ({
            'AccountID': g.accountId,
            'Name': g.fullName,
            'EmailAddress': g.email,
            'HomeAddress': g.address,
            'UserRole': g.usertype
        })
    return jsonify({"error": "Not logged in"}), 401


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get("email")
    plain_password = request.json.get("plain_password")

    # calling the login function from user.py
    res = user.loginAccount(email, plain_password)

    if res == "successful":
        session['email'] = email
        return jsonify({"message": "Successfully logged in"}), 200
    else:
        return jsonify({"error": res}), 401


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
        return jsonify({"message": "Successfully registered!"}), 201
    else:
        return jsonify({"error": "Registration failed."}), 409


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    res = user.logoutAccount()
    if res == "successful":
        session.clear()
        return jsonify({"message": "Successfully logged out!"}), 200
    else:
        return jsonify({"error": "Logout failed."}), 500

@app.route('/delete', methods=['POST'])
@login_required
def delete():
    try:
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM UserAccounts WHERE Email=?", (g.email,))
        connection.commit()
        session.clear()
        return jsonify({"message": "Successfully deleted account!"}), 200
    except:
        return jsonify({"error": "Deletion failed."}), 500
    

@app.route('/wishlist', methods=['POST'])
@login_required
def wishlist():
    return "bla"

if __name__ == '__main__':
    app.run(debug=True)