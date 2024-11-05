import sqlite3
import sys
from typing import List
from Product import Product
from Inventory import Inventory
from User import User


class Seller(User):
    def __init__(self):
        super().__init__()
        self.inventory = Inventory()
        self.cursor = self.inventory.cursor  # Use inventory's cursor for DB operations

    def createSellerAccount(self):
        self.CreateAccount()

        try:
            self.cursor.execute("INSERT INTO SellerAccounts (SellerID, Email, Password, StoreName) VALUES (?, ?, ?, ?)",
                                (self.UserID, self.Email, self.Password, self.StoreName))
            self.inventory.connection.commit()
            print("Seller account successfully created!")
        except sqlite3.Error as e:
            print(f"ERROR: An error occurred while inserting into SellerAccounts database: {e}")

    def addProduct(self, brand: str, name: str, stock_quantity: int, color: str, shoe_size: str, price: str) -> None:
        self.inventory.AddProduct(brand, name, stock_quantity, color, shoe_size, price)

    def viewListings(self, brand: str) -> List[str]:
        try:
            self.inventory.cursor.execute("SELECT * FROM Inventory WHERE Brand=?", (brand,))
            listings = self.inventory.cursor.fetchall()

            if not listings:
                print("No listings available for this brand.")
                return []  # Return an empty list if no listings are found
            else:
                print("Listings for Brand:", brand)
                for listing in listings:
                    print(f"ID: {listing[0]}, Brand: {listing[1]}, ItemName: {listing[2]}, Quantity: {listing[3]}, Size: {listing[4]}, Price: ${listing[2]}")
                return listings  # Return the listings
        except sqlite3.Error as e:
            print(f"ERROR: An error occurred while fetching listings: {e}")
            return []  # Return an empty list on error


    def updateListings(self, ItemID: str, Quantity: int, AddOrRemove: bool) -> None:
        self.inventory.UpdateStockQuantity(ItemID, Quantity, AddOrRemove)

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()