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

## Scenario 1: User successfully adds an item to their cart

def test_add_to_cart_success(client):
    populate_table()
    client = register_and_login(client)
    # Add an item to cart
    response = client.post('/cart/add', json={
        "itemName": "Shoe 1"
    })
    
    assert response.status_code == 201
    assert response.get_json()["message"] == "Item added to cart successfully"
    clear_table()

## Scenario 2: An Item is attemted to be added to the cart without a name

def test_add_to_cart_missing_item_name(client):
    client = register_and_login(client)
    
    # Try to add item without item name
    response = client.post('/cart/add', json={
        "quantity": 2
    })
    
    assert response.status_code == 400
    assert "error" in response.get_json()

## Scenario 3: User successfully removes an item from their cart

def test_remove_from_cart_success(client):
    client = register_and_login(client)
    populate_table()
    # Add an item to cart
    response = client.post('/cart/add', json={
        "itemName": "Shoe 1"
    })
    assert response.status_code == 201
    
    # Then fetch cart items to get the item ID
    cart_response = client.get('/cart/items')
    assert cart_response.status_code == 200
    items = cart_response.get_json()["items"]
    assert len(items) > 0
    
    # Remove the item
    remove_response = client.post('/cart/remove', json={
        "itemId": items[0]["itemId"]
    })
    
    assert remove_response.status_code == 200
    assert remove_response.get_json()["message"] == "Item removed from cart successfully"
    clear_table()

## Scenario 4: The user successfully updates the quantity of an item in their cart

def test_update_cart_quantity_success(client):
    client = register_and_login(client)
    populate_table()
    # Add an item to cart
    add_response = client.post('/cart/add', json={
        "itemName": "Shoe 1",
        "quantity": 2
    })
    assert add_response.status_code == 201
    
    # Fetch cart items to get the item ID
    cart_response = client.get('/cart/items')
    assert cart_response.status_code == 200
    items = cart_response.get_json()["items"]
    assert len(items) > 0
    
    # Update quantity
    update_response = client.put('/cart/update', json={
        "itemId": items[0]["itemId"],
        "quantity": 5
    })
    
    assert update_response.status_code == 200
    assert update_response.get_json()["message"] == "Quantity updated successfully"
    clear_table()

## Scenario 5: The user attemts to add more items that in stock when updating their cart

def test_update_cart_quantity_failure(client):
    client = register_and_login(client)
    populate_table()
    # Add an item to cart
    add_response = client.post('/cart/add', json={
        "itemName": "Shoe 1",
        "quantity": 2
    })
    assert add_response.status_code == 201
    
    # Fetch cart items to get the item ID
    cart_response = client.get('/cart/items')
    assert cart_response.status_code == 200
    items = cart_response.get_json()["items"]
    assert len(items) > 0
    
    # Update quantity
    update_response = client.put('/cart/update', json={
        "itemId": items[0]["itemId"],
        "quantity": 34
    })
    
    assert update_response.status_code == 400
    clear_table()

## Scenario 6: User successfully views their cart items

def test_get_cart_items(client):
    client = register_and_login(client)
    populate_table()
    # Add multiple items to cart
    client.post('/cart/add', json={"itemName": "Shoe 1", "quantity": 2})
    client.post('/cart/add', json={"itemName": "Shoe 2", "quantity": 3})
    
    # Fetch cart items
    response = client.get('/cart/items')
    
    assert response.status_code == 200
    cart_data = response.get_json()
    assert "items" in cart_data
    assert "total" in cart_data
    assert len(cart_data["items"]) > 0
    clear_table()
