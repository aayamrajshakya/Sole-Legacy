import sqlite3
import random
from User import User
import sys

# Todo Register Account
# Todo Login
# Todo Logout
# Todo Manage Account
# - Todo Update Account Info
# - Todo Delete Account
################################
# Todo Manage Inventory
# ---- Todo Edit Product Details

class Seller(User):
    def __init__(self):
        super().__init__()

        # Attempts to connect to the database
        try:
            self.connection = sqlite3.connect("StoreDatabase.db")
        except sqlite3.Error:
            print("ERROR: Failed to connect to the database")
            sys.exit()

        self.cursor = self.connection.cursor()
        self.StoreName: str = ""
        self.listing_id: str = ""
        self.price: float = 0.0
        self.description: str = ""

    def CreateSellerAccount(self):
        # Call User create Account
        self.CreatAccount()
        print(f"Testing SellerID: {self.UserID}, Email: {self.Email}, Password: {self.Password}")
        # Adds Store Name
        self.StoreName = input("Please enter your store name:\n")

        

        # Insert seller account into the database
        try:
            print(f"Inserting SellerID: {self.UserID}, Email: {self.Email}, Password: {self.Password}, StoreName: {self.StoreName}")
            self.cursor.execute("INSERT INTO SellerAccounts (SellerID, Email, Password, StoreName) VALUES (?, ?, ?, ?)",
                                (self.UserID, self.Email, self.Password, self.StoreName))
            self.connection.commit()
            print("Seller account successfully created!")
        except sqlite3.Error as e:
            print(f"ERROR: An error occurred while inserting into SellerAccounts database: {e}")

    def generate_unique_listing_id(self):
        while True:
            listing_id = str(random.randint(1000, 9999))
            self.cursor.execute("SELECT ListingID FROM Listings WHERE ListingID = ?", (listing_id,))
            result = self.cursor.fetchall()
            if not result:
                return listing_id

    def AddListing(self, item_name: str, price: float, description: str):
        listing_id = self.generate_unique_listing_id()
        try:
            print(f"Testing ListingID: {self.listing_id}, SellerID: {self.UserID}, Price: {self.price}, Description: {self.description}")
            self.cursor.execute("INSERT INTO Listings (ListingID, SellerID, Price, Description) VALUES (?, ?, ?, ?)",
                                (listing_id, self.UserID, price, description))  # ItemID can be set when adding items to inventory
            self.connection.commit()
            print(f"Listing added: {item_name} with ID: {listing_id}")
        except sqlite3.Error:
            print("ERROR: An error occurred while adding the listing to the database")

    def ViewListings(self):
        self.cursor.execute("SELECT * FROM Listings WHERE SellerID = ?", (self.UserID,))
        listings = self.cursor.fetchall()

        if not listings:
            print("No listings available.")
        else:
            print("Your Listings:")
            for listing in listings:
                print(f"ID: {listing[0]}, Price: ${listing[2]}, Description: {listing[3]}")

    def RemoveListing(self, listing_id: str):
        try:
            self.cursor.execute("DELETE FROM Listings WHERE ListingID = ? AND SellerID = ?", (listing_id, self.UserID))
            self.connection.commit()
            print(f"Listing with ID {listing_id} removed.")
        except sqlite3.Error:
            print("ERROR: An error occurred while removing the listing.")

    def __del__(self):
        self.cursor.close()
        self.connection.close()