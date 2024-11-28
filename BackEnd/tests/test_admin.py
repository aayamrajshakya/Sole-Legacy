import pytest
import sqlite3
from admin import Admin

# Fixture to create a new Admin instance for each test
@pytest.fixture
def admin_instance():
    return Admin()

# Fixture to provide a database connection
@pytest.fixture
def db_connection():
    connection = sqlite3.connect("StoreDatabase.db")  # Replace with your DB path
    yield connection
    connection.close()

def test_view_user_accounts(admin_instance, db_connection):
    # Arrange (optional): You might want to add some test users to the database
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO UserAccounts (FullName, Email, Password, Address, UserType) VALUES (?, ?, ?, ? , ?)",
                   ("Test User", "test@example.com", "test", "123 Main St", "Buyer"))
    db_connection.commit()
    result = admin_instance.viewUserAccounts()
    assert isinstance(result, list)
    assert len(result) > 0  # Check if at least one user is returned
    assert "Test User" in [user["FullName"] for user in result]  # Check if the test user is included

def test_add_product(admin_instance, db_connection):
    # Act
    result = admin_instance.addProduct(
        ItemName="Test Shoes",
        Description="Amazing test shoes",
        Image="test_image.jpg",
        Url="test-shoes",
        Quantity=10,
        Price="99.99",
        Gender="Unisex"
    )
    assert result == "successful"

def test_remove_product(admin_instance, db_connection):
    # Arrange: Add a test product to the database
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO Inventory (ItemName, Description, Image, Url, Quantity, Price, Gender) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   ("Test Shoes", "Amazing test shoes", "test_image.jpg", "test-shoes", 10, "99.99", "Unisex"))
    db_connection.commit()
    test_item_id = cursor.lastrowid  # Get the ID of the inserted product
    result = admin_instance.removeProduct(test_item_id)
    assert result == "successful"


def test_update_stock_quantity(admin_instance, db_connection):
    cursor = db_connection.cursor()
    result = admin_instance.updateStockQuantity(1, 5, True)  # Add 5 to quantity
    assert result == "successful"
    # Optionally, query the database to verify the quantity was updated