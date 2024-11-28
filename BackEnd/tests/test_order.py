import sqlite3

# Helper function for populating the inventory
def populate_table():
    connection = sqlite3.connect('StoreDatabase.db')
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Inventory (ItemId, ItemName, Description, Image, Url, Quantity, Price, Gender) 
        VALUES (1, 'Shoe 1', '(Description)', 'showcase_1.png', 'TestUrl', 30, 133.13, 'Men')
    """)

    cursor.execute("""
        INSERT INTO Inventory (ItemId, ItemName, Description, Image, Url, Quantity, Price, Gender) 
        VALUES (2, 'Shoe 2', '(Description)', 'showcase_2.png', 'TestUrl2', 40, 150.99, 'Men')
    """)

    connection.commit()
    cursor.close()
    connection.close()

# Helper function for clearing the inventory
def clear_table():
    connection = sqlite3.connect('StoreDatabase.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Inventory")
    connection.commit()
    cursor.close()
    connection.close()

# Helper function for registration and login
def register_and_login(client):
    # Register a test user
    client.post('/register', json={
        "fullName": "Test User",
        "email": "testuser@example.com",
        "plain_password": "Password123!",
        "address": "Test Address",
        "usertype": "Buyer"
    })
    
    # Login to get the session
    login_response = client.post('/login', json={
        "email": "testuser@example.com",
        "plain_password": "Password123!"
    })
    assert login_response.status_code == 200
    return client

## Scenario 1: User successfully adds an item to their cart and checks out

def test_process_checkout_success(client):
    client = register_and_login(client)
    populate_table()    

    # Add an item to cart first
    client.post('/cart/add', json={"itemName": "Shoe 1", "quantity": 1})
    
    # Attempt checkout
    response = client.post('/order/checkout', json={
        "cardNumber": "4111111111111111",
        "expiryDate": "12/25",
        "cvv": "123"
    })
    
    assert response.status_code == 200
    assert "orderID" in response.get_json()
    clear_table()

## Scenario 2: The User attempts to checkout without all credentials filled

def test_process_checkout_missing_card_details(client):
    client = register_and_login(client)
    populate_table()

    # Add an item to cart first
    client.post('/cart/add', json={"itemName": "Shoe 1", "quantity": 1})
    
    # Attempt checkout without full card details
    response = client.post('/order/checkout', json={
        "cardNumber": "4111111111111111"
    })
    
    assert response.status_code == 400
    assert "error" in response.get_json()
    clear_table()

## Scenario 3: The user successfully views their order details

def test_get_order_details(client):
    client = register_and_login(client)
    populate_table()

    # Add an item to cart and checkout to create an order
    client.post('/cart/add', json={"itemName": "Shoe 1", "quantity": 1})
    checkout_response = client.post('/order/checkout', json={
        "cardNumber": "4111111111111111",
        "expiryDate": "12/25",
        "cvv": "123"
    })
    order_id = checkout_response.get_json()["orderID"]
    
    # Fetch specific order details
    response = client.get(f'/order/{order_id}')
    
    assert response.status_code == 200
    order_details = response.get_json()
    assert "orderID" in order_details
    clear_table()

## Scenario 4: The user successfully makes 2 orders then views them

def test_get_user_orders(client):
    client = register_and_login(client)
    populate_table()

    # Create multiple orders
    client.post('/cart/add', json={"itemName": "Shoe 1", "quantity": 1})
    client.post('/order/checkout', json={
        "cardNumber": "4111111111111111",
        "expiryDate": "12/25",
        "cvv": "123"
    })
    
    client.post('/cart/add', json={"itemName": "Shoe 2", "quantity": 2})
    client.post('/order/checkout', json={
        "cardNumber": "4111111111111111",
        "expiryDate": "12/25",
        "cvv": "123"
    })
    
    # Fetch user orders
    response = client.get('/orders')
    
    assert response.status_code == 200
    orders_data = response.get_json()
    assert "orders" in orders_data
    assert len(orders_data["orders"]) > 0
    clear_table()