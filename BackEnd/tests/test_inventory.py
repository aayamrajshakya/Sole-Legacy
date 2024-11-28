import pytest
import sqlite3
from inventory import Inventory

# Fixture to create a new Inventory instance for each test
@pytest.fixture
def inventory_instance():
    return Inventory()

# Fixture to provide a database connection
@pytest.fixture
def db_connection():
    connection = sqlite3.connect("StoreDatabase.db")  # Replace with your DB path
    cursor = connection.cursor()
    yield connection
    connection.close()

def test_add_product(inventory_instance, db_connection):
    # Act
    result = inventory_instance.AddProduct(
        ItemName="Test Shoes",
        Description="Amazing test shoes",
        Image="test_image.jpg",
        Url="test-shoes",
        Quantity=10,
        Price="99.99",
        Gender="Unisex"
    )

    # Assert
    assert result is None  # AddProduct should return None on success
    # Optionally, query the database to verify the product was added

def test_remove_product(inventory_instance, db_connection):
    # Arrange: Add a test product to the database
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO Inventory (ItemName, Description, Image, Url, Quantity, Price, Gender) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   ("Test Shoes", "Amazing test shoes", "test_image.jpg", "test-shoes", 10, "99.99", "Unisex"))
    db_connection.commit()
    test_item_id = cursor.lastrowid  # Get the ID of the inserted product

    # Act
    result = inventory_instance.RemoveProduct(test_item_id)

    # Assert
    assert result == "successfully deleted"
    # Optionally, query the database to verify the product was removed

def test_remove_product_not_found(inventory_instance):
    # Act and Assert (expecting an exception)
    with pytest.raises(Exception) as e:
        inventory_instance.RemoveProduct(9999999)  # Assuming this ID doesn't exist
    assert "not found" in str(e.value)  # Check the exception message


def test_update_stock_quantity_remove_to_zero(inventory_instance, db_connection):
    # Arrange: Add a test product
    # ... (similar to test_remove_product)

    # Act
    inventory_instance.UpdateStockQuantity(1, 10, False)  # Remove all 10 from quantity
    cursor = db_connection.cursor()

    # Assert
    # Query the database to verify the product was removed
    cursor.execute("SELECT * FROM Inventory WHERE ItemID=?", (1,))
    result = cursor.fetchone()
    assert result is None  # Product should be deleted