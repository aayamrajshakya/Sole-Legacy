import sqlite3
import sys
from typing import List, Tuple, Optional
import random

class Cart:
    def __init__(self):
        self.databaseName = "StoreDatabase.db"
        self.connection = sqlite3.connect(self.databaseName, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def addItem(self, accountID: int, itemName: str, quantity: str):
        """Add item to cart with specified quantity"""
        try:
            # Try to convert the string quantity to an integer
            quantity = int(quantity)  # Convert quantity to an integer

        except ValueError:
            return "Invalid quantity value. It must be an integer."

        # Lookup ItemID using itemName
        self.cursor.execute(""" 
            SELECT ItemID, ItemName, Description, Image, Url, Quantity, Price, Gender
            FROM Inventory WHERE ItemName=? 
        """, (itemName,))
        
        item = self.cursor.fetchone()

        if not item:
            return "Item not found in inventory"

        itemID, itemName, description, image, url, inv_quantity, price, gender = item

        # Check if enough inventory is available
        if inv_quantity < quantity:
            return f"Insufficient inventory. Only {inv_quantity} available"

        # Check if item already exists in the cart for this account
        self.cursor.execute("""
            SELECT Quantity FROM Cart 
            WHERE AccountID=? AND ItemID=?
        """, (accountID, itemID))

        existing_item = self.cursor.fetchone()

        if existing_item:
            # If the item exists, update the quantity
            new_quantity = existing_item[0] + quantity
            self.cursor.execute("""
                UPDATE Cart 
                SET Quantity=? 
                WHERE AccountID=? AND ItemID=?
            """, (new_quantity, accountID, itemID))
        else:
            # Add a new item to the cart
            self.cursor.execute("""
                INSERT INTO Cart (AccountID, ItemID, ItemName, Description, Image, Quantity, Price, Gender)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (accountID, itemID, itemName, description, image, quantity, price, gender))

        # Commit the transaction to save changes
        self.connection.commit()
        return "Item added to cart successfully"

# cart.py additions

    def removeItem(self, itemID: str):
        """Remove item from cart"""
        try:
            itemID = int(itemID)
            self.cursor.execute("""
                DELETE FROM Cart 
                WHERE ItemID=?
            """, (itemID,))
            self.connection.commit()
            return "Item removed from cart successfully"
        except ValueError:
            return "Invalid item ID"
        except sqlite3.Error as e:
            return f"Database error: {str(e)}"

    def updateQuantity(self, itemID: int, quantity: int):
        """Update quantity of item in cart"""
        try:
            # Check if item exists in inventory and get current stock
            self.cursor.execute("""
                SELECT Quantity 
                FROM Inventory 
                WHERE ItemID=?
            """, (itemID,))
            
            inventory_item = self.cursor.fetchone()
            if not inventory_item:
                return "Item not found in inventory"
                
            if inventory_item[0] < quantity:
                return f"Insufficient inventory. Only {inventory_item[0]} available"

            # Update quantity in cart
            self.cursor.execute("""
                UPDATE Cart 
                SET Quantity=? 
                WHERE ItemID=?
            """, (quantity, itemID))
            
            self.connection.commit()
            return "Quantity updated successfully"
        except sqlite3.Error as e:
            return f"Database error: {str(e)}"

    def summarizeCart(self, accountID: int) -> List[Tuple]:
        """Get all items in cart with details"""
        try:
            self.cursor.execute("""
                SELECT ItemID, ItemName, Description, Image, Quantity, Price, Gender 
                FROM Cart 
                WHERE AccountID=?
            """, (accountID,))
            
            cart_items = self.cursor.fetchall()
            return cart_items
        except sqlite3.Error as e:
            return []

    def calculateTotal(self, accountID: int):
        """Calculate total price of all items in cart"""
        try:
            self.cursor.execute("""
                SELECT SUM(Quantity * Price) 
                FROM Cart 
                WHERE AccountID=?
            """, (accountID,))
            
            total = self.cursor.fetchone()[0]
            return float(total) if total else 0.0
        except sqlite3.Error as e:
            return 0.0


    # def __del__(self):
    #     """Destructor to clean up database connection"""
    #     try:
    #         if self.connection:
    #             # Only commit and close if the connection is open
    #             if self.connection:
    #                 self.connection.commit()
    #             if self.cursor:
    #                 self.cursor.close()
    #             self.connection.close()
    #     except:
    #         return ("Database already closed")