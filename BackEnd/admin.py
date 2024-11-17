import sqlite3
from typing import List, Dict, Optional, Union
from inventory import Inventory
from user import User

class Admin(User):
    def __init__(self):
        super().__init__()
        self.inventory = Inventory()
        self.connection = sqlite3.connect("StoreDatabase.db")
        self.cursor = self.connection.cursor()

    def loginAccount(self, email: str, password: str) -> str:
        """Authenticate admin credentials"""
        if self.loginAccount(email, password):
            self.cursor.execute("SELECT UserType FROM UserAccounts WHERE Email=?", (email,))
            result = self.cursor.fetchone()
            if result and result[0] == "Admin":
                self.is_authenticated = True
                return "successful"
        return "Invalid credentials"

    def logoutAccount(self):
        self.is_authenticated = False
        self.logoutAccount()
        return "successful"

    def viewUserAccounts(self) -> Union[List[Dict], str]:
        """View all user accounts in the system"""
        if not self.is_authenticated:
            return "Admin authentication required"
            
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

    def updateAccount(self, AccountID: str, parameter: str, newVal: str) -> str:
        if not self.is_authenticated:
            return "must log in as admin"
        else:
            self.updateAccount(AccountID, parameter, newVal)
            return "successful"

    def deleteAccount(self, AccountID: str) -> str:
        if not self.is_authenticated:
            return "must log in as admin"
        else:
            self.deleteAccount(AccountID)
            return "successful"

    def addProduct(self, Brand: str, ItemName: str, Description: str, Image: str, 
                   Quantity: int, Color: str, Size: str, Price: str, Gender: str) -> str:
        if not self.is_authenticated:
            return "must log in as admin"
        else:
            self.inventory.AddProduct(Brand, ItemName, Description, Image, Quantity, Color, Size, Price, Gender)
            return "successful"

    def removeProduct(self, ItemID: str) -> str:
        if not self.is_authenticated:
            return "must log in as admin"
        else:
            self.inventory.RemoveProduct(ItemID)
            return "successful"

    def updateStockQuantity(self, ItemID: str, Quantity: int, AddOrRemove: bool) -> str:
        if not self.is_authenticated:
            return "must log in as admin"
        else:
            self.inventory.UpdateStockQuantity(ItemID, Quantity, AddOrRemove)
            return "successful"

    def __del__(self):
        self.connection.close()
        self.cursor.close()
