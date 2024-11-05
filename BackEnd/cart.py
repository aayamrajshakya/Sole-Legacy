import sqlite3
import sys
from typing import List, Tuple, Optional

class Cart:
    def __init__(self, AccountID: str):
        self.AccountID = AccountID
        self.databaseName = "StoreDatabase.db"
        try:
            self.connection = sqlite3.connect(self.databaseName)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            print(f"ERROR: {error}")
            sys.exit()

    def addItem(self, itemID: str, quantity: str = '1') -> str:
        """Add item to cart with specified quantity"""
        try:
            quantity = int(quantity)  # Convert quantity to an integer

            # Check if item exists in inventory and get its details
            self.cursor.execute("""
                SELECT ItemName, Brand, Price, Color, Size, Quantity 
                FROM Inventory WHERE ItemID=?
            """, (itemID,))
            item = self.cursor.fetchone()
            
            if not item:
                return "Item not found in inventory"
            
            itemName, brand, price, color, size, inv_quantity = item
            
            if inv_quantity < quantity:
                return f"Insufficient inventory. Only {inv_quantity} available"
            
            # Check if item already exists in cart
            self.cursor.execute("""
                SELECT Quantity FROM Cart 
                WHERE AccountID=? AND ItemID=?
            """, (self.AccountID, itemID))
            
            existing_item = self.cursor.fetchone()
            
            if existing_item:
                # Update quantity if item exists
                new_quantity = existing_item[0] + quantity
                self.cursor.execute("""
                    UPDATE Cart 
                    SET Quantity=? 
                    WHERE AccountID=? AND ItemID=?
                """, (new_quantity, self.AccountID, itemID))
            else:
                # Add new item to cart
                self.cursor.execute("""
                    INSERT INTO Cart (AccountID, ItemID, ItemName, Brand, Price, Color, Size, Quantity)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (self.AccountID, itemID, itemName, brand, price, color, size, quantity))
            
            self.connection.commit()
            return "Item added successfully"
            
        except sqlite3.Error as error:
            return f"Error adding item: {error}"
        except ValueError:
            return "Invalid quantity value. It must be an integer."

    def removeItem(self, itemID: str) -> str:
        """Remove item from cart"""
        try:
            self.cursor.execute("""
                DELETE FROM Cart 
                WHERE AccountID=? AND ItemID=?
            """, (self.AccountID, itemID))
            
            if self.cursor.rowcount == 0:
                return "Item not found in cart"
            
            self.connection.commit()
            return "Item removed successfully"
            
        except sqlite3.Error as error:
            return f"Error removing item: {error}"

    def updateQuantity(self, itemID: int, quantity: int) -> str:
        """Update quantity of item in cart"""
        try:
            # Check inventory
            self.cursor.execute("""
                SELECT Quantity 
                FROM Inventory 
                WHERE ItemID=?
            """, (itemID,))
            
            inv_quantity = self.cursor.fetchone()
            
            if not inv_quantity or inv_quantity[0] < quantity:
                return f"Insufficient inventory. Only {inv_quantity[0]} available"
            
            self.cursor.execute("""
                UPDATE Cart 
                SET Quantity=? 
                WHERE AccountID=? AND ItemID=?
            """, (quantity, self.AccountID, itemID))
            
            if self.cursor.rowcount == 0:
                return "Item not found in cart"
            
            self.connection.commit()
            return "Quantity updated successfully"
            
        except sqlite3.Error as error:
            return f"Error updating quantity: {error}"

    def summarizeCart(self) -> List[Tuple]:
        """Return summary of cart items"""
        try:
            self.cursor.execute("""
                SELECT ItemName, Brand, Color, Size, Quantity 
                FROM Cart 
                WHERE AccountID=?
            """, (self.AccountID,))
            return self.cursor.fetchall()
        except sqlite3.Error as error:
            print(f"Error summarizing cart: {error}")
            return []

    def calculateTotal(self) -> float:
        """Calculate total price of items in cart"""
        try:
            self.cursor.execute("""SELECT SUM(Cart.Price * Cart.Quantity) 
                                FROM Cart 
                                WHERE Cart.AccountID=?""", (self.AccountID,))
            total = self.cursor.fetchone()[0]
            return total if total else 0.0
                
        except sqlite3.Error as error:
                print(f"Error calculating total: {error}")
                return 0.0

    def __del__(self):
        """Destructor to clean up database connection"""
        self.connection.commit()
        self.cursor.close()
        self.connection.close()