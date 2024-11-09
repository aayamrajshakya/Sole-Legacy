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
            g.accountID = user_details[0]
            g.fullName = user_details[1]
            g.password = user_details[3]
            g.address = user_details[4]
            g.usertype = user_details[5]
        else:
            g.accountID = None
            g.fullName = None
            g.address = None
            g.usertype = None


@app.route('/dashboard')
@login_required
def dashboard():
    if g.email:
        return jsonify ({
            'AccountID': g.accountID,
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
    

@app.route('/wishlist', methods=['GET'])
@login_required
def fetchWishlist():
    try:
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        cursor.execute("SELECT ItemName, Price, Color, Size, Gender, Slug FROM Wishlist WHERE AccountID=?", (g.accountID,))
        wholeWishlist = cursor.fetchall()
        if not wholeWishlist:
            return jsonify({"message": "Wishlist is empty", "items": []}), 200
        items=[]
        for indivItem in wholeWishlist:
            ItemName, Price, Color, Size, Gender, Slug = indivItem
            items.append({"ItemName": ItemName, "Price": Price, "Color": Color, "Size": Size, "Gender": Gender, "Slug": Slug})
        return jsonify({"message": "Wishlist fetched", "items": items}), 200
    except:
        return jsonify({"error": "Wishlist fetching failed."}), 500


@app.route('/removeFromWishlist', methods=['POST'])
@login_required
def removeFromWishlist():
    try:
        itemName = request.json.get('ItemName')
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Wishlist WHERE ItemName=?", (itemName,))
        connection.commit()
        return jsonify({"message": f"Successfully deleted {itemName} from wishlist!"}), 200
    except:
        return jsonify({"error": "Deletion failed."}), 500
    

@app.route('/addToWishlist', methods=['POST'])
@login_required
def addToWishlist():
    try:
        ItemName = request.json.get("ItemName")
        Price = request.json.get("Price")
        Color = request.json.get("Color")
        Size = request.json.get("Size")
        Gender = request.json.get("Gender")
        Slug = request.json.get("Slug")
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        # check if the item is already in wishlist
        cursor.execute("SELECT * FROM Wishlist WHERE AccountID=? AND ItemName=?", (g.accountID, ItemName))
        pointer = cursor.fetchone()
        if pointer:
            return jsonify({"message": "Item already in wishlist"}), 200
        # if not, then add
        cursor.execute("INSERT INTO Wishlist(AccountID, ItemName, Price, Color, Size, Gender, Slug) VALUES (?, ?, ?, ?, ?, ?, ?)",(g.accountID, ItemName, Price, Color, Size, Gender, Slug))
        connection.commit()
        return jsonify({"message": "Successfully added to wishlist"}), 200
    except:
        return jsonify({"error": "Wishlist action failed"}), 500


@app.route('/shoes/women', methods=['GET'])
def womenShoes():
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        cursor.execute("SELECT ItemName, Description, Image, Url, Price, Gender FROM Inventory WHERE Gender='Women'")
        women_ptr = cursor.fetchall()
        items=[]
        for indivItem in women_ptr:
            ItemName, Description, Image, Url, Price, Gender = indivItem
            items.append({"ItemName": ItemName, "Description": Description, "Image": Image, "Url": Url, "Price": Price, "Gender": Gender})
        return jsonify(items)


@app.route('/shoes/men', methods=['GET'])
def menShoes():
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        cursor.execute("SELECT ItemName, Description, Image, Url, Price, Gender FROM Inventory WHERE Gender='Men'")
        men_ptr = cursor.fetchall()
        items=[]
        for indivItem in men_ptr:
            ItemName, Description, Image, Url, Price, Gender = indivItem
            items.append({"ItemName": ItemName, "Description": Description, "Image": Image, "Url": Url, "Price": Price, "Gender": Gender})
        return jsonify(items)


@app.route('/shoes/showcase', methods=['GET'])
def showcaseShoes():
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        cursor.execute("SELECT ItemName, Description, Image, Url, Price, Gender FROM Inventory WHERE Image LIKE '%showcase%'")
        showcase_ptr = cursor.fetchall()
        items=[]
        for indivItem in showcase_ptr:
            ItemName, Description, Image, Url, Price, Gender = indivItem
            items.append({"ItemName": ItemName, "Description": Description, "Image": Image, "Url": Url, "Price": Price, "Gender": Gender})
        return jsonify(items)


@app.route('/shoe/<string:url>', methods=['GET'])
def indivShoe(url):
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        cursor.execute("SELECT ItemName, Description, Image, Url, Price, Gender FROM Inventory WHERE Url=?", (url,))
        indiv_ptr = cursor.fetchone()
        ItemName, Description, Image, Url, Price, Gender = indiv_ptr
        items = {"ItemName": ItemName, "Description": Description, "Image": Image, "Url": Url, "Price": Price, "Gender": Gender}
        return jsonify(items)


@app.route('/search', methods=['POST'])
def search_items():
        searchKeyword = request.json.get("searchKeyword")
        try:   
            connection = sqlite3.connect("StoreDatabase.db")
            cursor = connection.cursor()
            cursor.execute("SELECT ItemID, ItemName, Image, Url, Price, Gender FROM Inventory WHERE ItemName LIKE ?", ('%' + searchKeyword + '%',))
            searchedItems = cursor.fetchall()
            if not searchedItems:
                return jsonify({"message": "No such item"}), 200
            items = []
            for indivItem in searchedItems:
                    ItemID, ItemName, Image, Url, Price, Gender = indivItem
                    items.append({"ItemID": ItemID, "ItemName": ItemName, "Image": Image, "Url": Url, "Price": Price, "Gender": Gender})
            return jsonify({"message": "Search results posted", "items": items}), 200
        except:
             return jsonify({"error": "Search failed"}), 500
        

if __name__ == '__main__':
    app.run(debug=True)