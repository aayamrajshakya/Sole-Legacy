import os
import pytest
import sqlite3
from app import app
from db_init import initialize_database

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Ttest database
    # since our db_init has a static name --> StoreDatabase.db, we have to set the test db name as such too
    test_database = 'StoreDatabase.db'
    
    # initialize the test database
    connection = sqlite3.connect(test_database)
    cursor = connection.cursor()
    initialize_database()
    cursor.close()
    connection.close()

    yield

    # delete the test database after each test instance
    if os.path.exists(test_database):
        os.remove(test_database)

@pytest.fixture(scope="function")
def client():
    with app.test_client() as client:
        yield client
