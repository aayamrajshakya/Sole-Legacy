import sqlite3
import sys
from typing import List, Dict, Optional, Union
from inventory import Inventory
from user import User

class Admin(User):
    def __init__(self):
        super().__init__()
        self.inventory = Inventory()
        try:
            self.connection = sqlite3.connect("StoreDatabase.db")
            self.cursor = self.connection.cursor()

        except sqlite3.error as error:
            print(f"{error}")
            sys.exit()



    def viewUserAccounts(self) -> Union[List[Dict], str]:
        """View all user accounts in the system"""
        # if not self.is_authenticated:
        #     return "Admin authentication required"
        #
        try:
            self.cursor.execute("SELECT AccountID, FullName, Email, Address, UserType FROM UserAccounts")
            rows = self.cursor.fetchall()
            
            users = []
            for row in rows:
                users.append({
                    "AccountID": row[0],
                    "FullName": row[1],
                    "Email": row[2],
                    "Address": row[3],
                    "UserType": row[4]
                })
            return users
            
        except sqlite3.Error as error:
            return f"Error: {error}"

    def addProduct(self, ItemName: str, Description: str, Image: str, Url: str, Quantity: int, Price: str, Gender: str) -> str:
        Inventory().AddProduct(ItemName, Description, Image, Url , Quantity, Price, Gender)
        return "successful"

    def removeProduct(self, ItemID: str) -> str:
        Inventory().RemoveProduct(ItemID)
        return "successful"

    def updateStockQuantity(self, ItemID: str, Quantity: int, AddOrRemove: bool) -> str:
        Inventory().UpdateStockQuantity(ItemID, Quantity, AddOrRemove)
        return "successful"

    # def __del__(self):
    #     self.connection.close()
    #     self.cursor.close()
