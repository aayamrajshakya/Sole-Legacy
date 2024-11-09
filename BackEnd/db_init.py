import sqlite3
import json

def initialize_database():
    try:
        connection = sqlite3.connect('StoreDatabase.db')
        cursor = connection.cursor()

        # using AUTOINCREMENT for generating unique IDs: https://www.w3schools.com/SQl/sql_autoincrement.asp

        tables = {
            "Inventory": """CREATE TABLE IF NOT EXISTS Inventory (
                          ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
                          ItemName VARCHAR(80) NOT NULL,
                          Description TEXT NOT NULL,
                          Image TEXT NOT NULL,
                          Url TEXT NOT NULL,
                          Quantity INTEGER NOT NULL,
                          Price FLOAT NOT NULL,
                          Gender TEXT NOT NULL,
                          )""",

            "UserAccounts": """CREATE TABLE IF NOT EXISTS UserAccounts (
                             AccountID INTEGER PRIMARY KEY AUTOINCREMENT,
                             FullName TEXT NOT NULL,
                             Email TEXT NOT NULL UNIQUE,
                             Password TEXT NOT NULL,
                             Address TEXT NULL,
                             UserType TEXT NOT NULL
                             )""",

            "AdminAccounts": """CREATE TABLE IF NOT EXISTS AdminAccounts (
                              AdminID INTEGER PRIMARY KEY AUTOINCREMENT,
                              Email VARCHAR(80) NOT NULL UNIQUE,
                              Password VARCHAR(80) NOT NULL
                              )""",

            "SellerAccounts": """CREATE TABLE IF NOT EXISTS SellerAccounts (
                               SellerID INTEGER PRIMARY KEY AUTOINCREMENT,
                               Email VARCHAR(80) NOT NULL UNIQUE,
                               Password VARCHAR(80) NOT NULL
                               )""",

            "Orders": """CREATE TABLE IF NOT EXISTS Orders (
                       OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
                       AccountID INTEGER NOT NULL,
                       OrderDate DATETIME NOT NULL,
                       AmountTotal FLOAT NOT NULL,
                       FOREIGN KEY (AccountID) REFERENCES UserAccounts(AccountID)
                       )""",

            "OrderItems": """CREATE TABLE IF NOT EXISTS OrderItems (
                           OrderID INTEGER NOT NULL,
                           ItemID INTEGER NOT NULL,
                           ItemName VARCHAR(80),
                           Quantity INTEGER NOT NULL,
                           FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
                           FOREIGN KEY (ItemID) REFERENCES Inventory(ItemID)
                           )""",

            "Wishlist": """CREATE TABLE IF NOT EXISTS Wishlist (
                         AccountID INTEGER NOT NULL,
                         ItemName VARCHAR(80) NOT NULL,
                         Price FLOAT NOT NULL,
                         Color VARCHAR(25) NOT NULL,
                         Size VARCHAR(30) NOT NULL,
                         Gender VARCHAR(10) NOT NULL,
                         Slug TEXT NOT NULL,                
                         FOREIGN KEY (AccountID) REFERENCES UserAccounts(AccountID)
                         )"""
        }

        # iterative function to create tables
        for table, query in tables.items():
            cursor.execute(query)

    except sqlite3.Error as error:
        print(f"ERROR: {error}")

    finally:    
        cursor.close()
        connection.close()

if __name__ == "__main__":
    initialize_database()


#  FOREIGN KEY (ItemID) REFERENCES Inventory(ItemID),
