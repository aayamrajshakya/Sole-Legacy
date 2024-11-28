import json
import pytest

# Helper function for seller registration
def seller_registration_helper(client):
    return client.post('/register', json={
        "fullName": "Test Seller",
        "email": "testseller@msu.edu", 
        "plain_password": "SellerPassword123!",
        "address": "Test Address",
        "usertype": "Seller"
    })

# Helper function for seller login
def seller_login_helper(client):
    return client.post('/login', json={
        "email": "testseller@msu.edu",
        "plain_password": "SellerPassword123!"
    })

## Scenario 1: Seller adds Product successfully

def test_add_product_success(client):
    # First, register and login as a seller
    seller_registration_helper(client)
    seller_login_helper(client)

    # Prepare product data
    product_data = {
        "itemName": "Test Product",
        "description": "A test product description",
        "image": "test-image.jpg",
        "url": "https://testproduct.com",
        "quantity": 10,
        "price": 29.99,
        "gender": "Male"
    }

    # Add product
    response = client.post('/seller/product', json=product_data)
    
    # Assert successful product addition
    assert response.status_code == 201
    response_json = response.get_json()
    assert response_json["message"] == "Product added successfully"
    # assert "itemId" in response_json

## Scenario 2: Seller attempts to add product without all credentials filled out

def test_add_product_missing_fields(client):
    # First, register and login as a seller
    seller_registration_helper(client)
    seller_login_helper(client)

    # Prepare incomplete product data
    product_data = {
        "itemName": "Incomplete Product",
        "description": "A test product description",
        # Intentionally missing some required fields
    }

    # Attempt to add product
    response = client.post('/seller/product', json=product_data)
    
    # Assert error for missing fields
    assert response.status_code == 400
    assert "All fields are required" in response.get_json()["error"]

## Scenario 3: Seller successfully views their listings
def test_view_listings_success(client):
    seller_registration_helper(client)
    seller_login_helper(client)

    # Add a product
    product_data = {
        "itemName": "SearchProduct",
        "description": "A test product for search",
        "image": "search-image.jpg",
        "url": "https://searchproduct.com",
        "quantity": 5,
        "price": 19.99,
        "gender": "Male"
    }
    client.post('/seller/product', json=product_data)

    # Search for the product
    response = client.get('/seller/listings?itemName=SearchProduct')
    
    # Assert successful listing retrieval
    assert response.status_code == 200
    json_response = response.get_json()
    assert len(json_response['listings']) > 0
    assert json_response['listings'][0]['ItemName'] == "SearchProduct"

## Scenario 4: User attempts to remove a product without a valid id

def test_remove_product_missing_id(client):
    # First, register and login as a seller
    seller_registration_helper(client)
    seller_login_helper(client)

    # Attempt to remove product without ItemID
    remove_response = client.post('/seller/remove-product', json={})
    
    # Assert error for missing ItemID
    assert remove_response.status_code == 400
    assert "ItemID is required" in remove_response.get_json()["error"]
