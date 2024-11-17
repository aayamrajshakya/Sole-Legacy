import sqlite3
import sys
from typing import List, Dict, Optional, Union
from product import Product
from inventory import Inventory
from user import User


class Seller(User):
    def __init__(self):
        super().__init__()
        self.inventory = Inventory()
        self.connection = sqlite3.connect("StoreDatabase.db")
        self.cursor = self.connection.cursor()
    
    def viewListings(self, ItemName: str):

        try:
            self.cursor.execute("SELECT * FROM Inventory WHERE ItemName=?", (ItemName,))
            rows = self.cursor.fetchall()

            listings = []
            for row in rows:
                listings.append({
                    "ItemID": row[0],
                    "ItemName": row[1],
                    "Description": row[2],
                    "Image": row[3],
                    "Quantity": row[4],
                    "Price": row[5],
                    "Gender": row[6]
                })
            return listings
        
        except sqlite3.Error as error:
            return f"Error: {error}"

    def AddProduct(self, ItemName: str, Description: str, Image: str, Url: str, Quantity: int, Price: str, Gender: str):
        try:
            self.inventory.AddProduct(ItemName, Description, Image, Url, Quantity, Price, Gender)
            return "successful"
        except sqlite3.Error as error:
            return f"Error: {error}"

    def RemoveProduct(self, ItemID: str):
        try:
            self.inventory.RemoveProduct(ItemID)
            return "successful"
        except sqlite3.Error as error:
            return f"Error: {error}"
        
    def UpdateStockQuantity(self, ItemID: str, Quantity: int, AddOrRemove: bool):
        try:
            self.inventory.UpdateStockQuantity(ItemID, Quantity, AddOrRemove)
            return "successful"
        except sqlite3.Error as error:
            return f"Error: {error}"
        
    # def __del__(self):
    #     self.connection.close()
    #     self.cursor.close()
