import sqlite3
import sys

# Test connection to database
try:
    connection = sqlite3.connect('StoreDatabase.db')

# If connection fails then exit program
except sqlite3.Error as error:
    print(f"ERROR: {error}")
    sys.exit()

cursor = connection.cursor()

# Inventory database query
Inventory: str = """CREATE TABLE IF NOT EXISTS Inventory (
                  ItemID INTEGER NOT NULL,
                  Brand VARCHAR(50) NOT NULL,
                  ItemName VARCHAR(80) NOT NULL,
                  Description TEXT NOT NULL,
                  Image TEXT NOT NULL,
                  Quantity INTEGER NOT NULL,
                  Color VARCHAR(25) NOT NULL,
                  Size VARCHAR(30) NOT NULL,
                  PRIMARY KEY(ItemID)
                  )"""

# Account database query
UserAccounts: str = """CREATE TABLE IF NOT EXISTS UserAccounts (
                     AccountID INTEGER NOT NULL UNIQUE,
                     FullName TEXT NOT NULL,
                     Email VARCHAR(80) NOT NULL UNIQUE,
                     Password VARCHAR(80) NOT NULL,
                     Address VARCHAR(255),
                     UserType VARCHAR(10) NOT NULL,
                     PRIMARY KEY (AccountID)
                     )"""   

# Admin Account database query
AdminAccounts: str = """CREATE TABLE IF NOT EXISTS AdminAccounts (
                      AdminID INTEGER NOT NULL,
                      Email VARCHAR(80) NOT NULL UNIQUE,
                      Password VARCHAR(80) NOT NULL,
                      PRIMARY KEY (AdminID)
                      )"""

# Seller Account database query
SellerAccounts: str = """CREATE TABLE IF NOT EXISTS SellerAccounts (
                       SellerID INTEGER NOT NULL,
                       Email VARCHAR(80) NOT NULL UNIQUE,
                       Password VARCHAR(80) NOT NULL,
                       PRIMARY KEY (SellerID)
                       )"""

# Orders Database Query
Orders: str = """CREATE TABLE IF NOT EXISTS Orders (
               OrderID INTEGER NOT NULL,
               AccountId INTEGER NOT NULL,
               OrderDate VARCHAR(10) NOT NULL,
               AmountTotal FLOAT NOT NULL,
               PRIMARY KEY (OrderID),
               FOREIGN KEY (AccountID) REFERENCES UserAccounts(AccountID)
               )"""

# Child table for Order items
OrderItems: str = """CREATE TABLE IF NOT EXISTS Order_items (
                   OrderID INTEGER NOT NULL,
                   ItemID INTEGER NOT NULL,
                   ItemName VARCHAR(80),
                   Quantity INTEGER NOT NULL,
                   FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
                   FOREIGN KEY (ItemID) REFERENCES Inventory(ItemID)
                   )"""

Wishlist= """CREATE TABLE IF NOT EXISTS Wishlist (
             ItemID INTEGER NOT NULL,
             ItemName VARCHAR(80) NOT NULL,
             Brand VARCHAR(50) NOT NULL,
             Price FLOAT NOT NULL,
             Color VARCHAR(25) NOT NULL,
             Size FLOAT NOT NULL,
             FOREIGN KEY (ItemID) REFERENCES Inventory(ItemID),
             FOREIGN KEY (AccountID) REFERENCES UserAccounts(AccountID)
             )"""

# attempts to create the required tables for database
try:
    cursor.execute(Inventory)
    cursor.execute(UserAccounts)
    cursor.execute(AdminAccounts)
    cursor.execute(SellerAccounts)
    cursor.execute(Orders)
    cursor.execute(OrderItems)
    cursor.execute(Wishlist)

# Send error if there is an issue within the database
except sqlite3.Error as error:
    print(f"ERROR: {error}")


connection.commit()
cursor.close()
connection.close()