# Much help from: https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/

from flask import Flask, request, jsonify, session, g
from flask_cors import CORS
from user import User
from seller import Seller
from inventory import Inventory
from cart import Cart
from order import Order
from functools import wraps
import sqlite3
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

app.secret_key = 'canputanythinghere'
user = User()
seller = Seller()
inventory = Inventory()
cart = Cart()
order = Order()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return jsonify({"error": "Log in first!"}), 401
        return f(*args, **kwargs)
    return decorated_function

def seller_required(f):
    """Decorator to ensure the logged-in user is a seller."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.usertype != "Seller":
            return jsonify({"error": "Must be logged in as a seller"}), 403
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

    if res[0] == "successful":
        session['email'] = email
        session['usetype'] = res[1]
        return jsonify({"message": "Successfully logged in", "regUserType": res[1]}), 200
    else:
        return jsonify({"error": res[0]}), 401


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


@app.route('/cart/add', methods=['POST'])
@login_required
def add_to_cart():
    try:
        # Get request parameters
        item_name = request.json.get("itemName")
        quantity = request.json.get("quantity", 1)

        # Validate required fields
        if not all([item_name, quantity]):
            return jsonify({"error": "Item name and quantity are required"}), 400

        # Call the Cart class method
        result = cart.addItem(g.accountID, item_name, str(quantity))
        
        if result == "Item added to cart successfully":
            return jsonify({"message": result}), 201
        else:
            return jsonify({"error": result}), 400

    except Exception as e:
        logging.error(f"Error adding item to cart: {str(e)}")
        return jsonify({"error": "Server error while adding item to cart"}), 500
    

@app.route('/cart/remove', methods=['POST'])
@login_required
def remove_from_cart():
    try:
        item_id = request.json.get("itemId")
        if not item_id:
            return jsonify({"error": "Item ID is required"}), 400
            
        result = cart.removeItem(item_id)
        
        if result == "Item removed from cart successfully":
            return jsonify({"message": result}), 200
        else:
            return jsonify({"error": result}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/update', methods=['PUT'])
@login_required
def update_cart_quantity():
    try:
        item_id = request.json.get("itemId")
        quantity = request.json.get("quantity")
        
        if not all([item_id, quantity]):
            return jsonify({"error": "Item ID and quantity are required"}), 400
            
        result = cart.updateQuantity(item_id, quantity)
        
        if result == "Quantity updated successfully":
            return jsonify({"message": result}), 200
        else:
            return jsonify({"error": result}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/items', methods=['GET'])
@login_required
def get_cart_items():
    try:
        items = cart.summarizeCart(g.accountID)
        total = cart.calculateTotal(g.accountID)
        
        return jsonify({
            "items": [
                {
                    "itemId": item[0],
                    "name": item[1],
                    "description": item[2],
                    "image": item[3],
                    "quantity": item[4],
                    "price": item[5],
                    "gender": item[6]
                } for item in items
            ],
            "total": total
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/order/checkout', methods=['POST'])
@login_required
def process_checkout():
    try:
        # Extract credit card details from the request body
        card_number = request.json.get('cardNumber')
        expiry_date = request.json.get('expiryDate')
        cvv = request.json.get('cvv')

        if not card_number or not expiry_date or not cvv:
            return jsonify({"error": "All credit card details are required"}), 400

        # Process the credit card payment here (e.g., using an external service like Stripe, etc.)
        payment_result = order.processPayment(card_number, expiry_date, cvv)
        if payment_result != "Payment processed successfully":
            return jsonify({"error": payment_result}), 400

        # Complete the checkout
        result = order.checkout(g.accountID)
        if isinstance(result, dict) and "orderID" in result:
            return jsonify(result), 200
        else:
            return jsonify({"error": result}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/order/<int:order_id>', methods=['GET'])
@login_required
def get_order(order_id):
    try:
        result = order.getOrderDetails(order_id)
        if isinstance(result, dict):
            return jsonify(result), 200
        else:
            return jsonify({"error": result}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/orders', methods=['GET'])
@login_required
def get_user_orders():
    try:
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT OrderID, OrderDate, AmountTotal
            FROM Orders
            WHERE AccountID = ?
            ORDER BY OrderDate DESC
        """, (g.accountID,))
        
        orders = cursor.fetchall()
        return jsonify({
            "orders": [{
                "orderID": order[0],
                "orderDate": order[1],
                "totalAmount": order[2]
            } for order in orders]
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/seller/product', methods=['POST'])
@login_required
@seller_required
def add_product():
    
    try:
        item_name = request.json.get("itemName")
        description = request.json.get("description")
        image = request.json.get("image")
        url = request.json.get("url")
        quantity = request.json.get("quantity")
        price = request.json.get("price")
        gender = request.json.get("gender")

        # Validate required fields
        if not all([item_name, description, image, url, quantity, price, gender]):
            return jsonify({"error": "All fields are required"}), 400

        # Call the Seller class method
        result = seller.AddProduct(item_name, description, image, url, quantity, price, gender)
        
        if result == "successful":
            return jsonify({"message": "Product added successfully"}), 201
        else:
            return jsonify({"error": "Failed to add product"}), 500

    except Exception as e:
        logging.error(f"Error adding product: {str(e)}")
        return jsonify({"error": "Server error while adding product"}), 500

@app.route('/seller/listings', methods=['GET'])
@login_required
@seller_required
def view_listings():
    item_name = request.args.get('itemName')
    if not item_name:
        return jsonify({
            'error': 'item_name parameter is required',
            'listings': []
        }), 400

    try:
        connection = sqlite3.connect("StoreDatabase.db")
        cursor = connection.cursor()
        
        query = "SELECT * FROM Inventory WHERE itemName LIKE ?"
        cursor.execute(query, ('%' + item_name + '%',))
        rows = cursor.fetchall()
        
        listings = []
        for row in rows:
            listings.append({
                "ItemID": row[0],
                "ItemName": row[1],
                "Description": row[2],
                "Image": row[3],
                "Url": row[4],
                "Quantity": row[5],
                "Price": row[6],
                "Gender": row[7]
            })
            
        cursor.close()

        return jsonify({
            'listings': listings,
            'message': f'Found {len(listings)} listings for {item_name}'
        })
    
    except sqlite3.Error as error:
        return jsonify({
            'error': f'Database error: {str(error)}',
            'listings': []
        }), 500
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}',
            'listings': []
        }), 500

@app.route('/seller/remove-product', methods=['POST'])
@login_required
@seller_required
def remove_product():

    try:
        item_id = request.json.get("ItemID")

        if not item_id:
            return jsonify({"error": "ItemID is required"}), 400
        
        result = inventory.RemoveProduct(item_id)
        
        if result == "successful":
            return jsonify({"message": "Product removed successfully"}), 200
        else:
            return jsonify({"error": result}), 500

    except Exception as e:
        logging.error(f"Error removing product: {str(e)}")
        return jsonify({"error": "Server error while removing product"}), 500


@app.route('/seller/update-stock', methods=['POST'])
@login_required
@seller_required
def update_stock():
    
    try:
        item_id = request.json.get("ItemID")
        quantity = request.json.get("Quantity")
        add_or_remove = request.json.get("AddOrRemove")  # True for adding stock, False for removing stock
        
        if not item_id or quantity is None or add_or_remove is None:
            return jsonify({"error": "ItemID, Quantity, and AddOrRemove are required"}), 400
        
        result = inventory.UpdateStockQuantity(item_id, quantity, add_or_remove)
        
        if result == "successful":
            return jsonify({"message": "Stock quantity updated successfully"}), 200
        else:
            return jsonify({"error": result}), 500

    except Exception as e:
        logging.error(f"Error updating stock: {str(e)}")
        return jsonify({"error": "Server error while updating stock"}), 500


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