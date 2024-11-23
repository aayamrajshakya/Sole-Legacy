import sqlite3
import random
from datetime import datetime
from inventory import Inventory

class Order:
    def __init__(self):
        self.databaseName = "StoreDatabase.db"
        self.inventory = Inventory()

    def processPayment(self, card_number: str, expiry_date: str, cvv: str):
        if len(card_number) != 16 or not card_number.isdigit():
            return "Invalid card number"
        if len(expiry_date) != 5 or not expiry_date[2] == '/' or not expiry_date.replace('/', '').isdigit():
            return "Invalid expiry date"
        if len(cvv) != 3 or not cvv.isdigit():
            return "Invalid CVV"

        return "Payment processed successfully"

    def getOrderDetails(self, orderID: int):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()
            
            # Get order items
            cursor.execute("""
                SELECT oi.OrderID, oi.ItemID, oi.ItemName, oi.Quantity, o.OrderDate, o.AmountTotal
                FROM OrderItems oi
                JOIN Orders o ON oi.OrderID = o.OrderID
                WHERE oi.OrderID = ?
            """, (orderID,))
            
            items = cursor.fetchall()
            if not items:
                return "Order not found"
                
            return {
                "orderID": items[0][0],
                "orderDate": items[0][4],
                "totalAmount": items[0][5],
                "items": [{
                    "itemID": item[1],
                    "itemName": item[2],
                    "quantity": item[3]
                } for item in items]
            }
            
        except sqlite3.Error as error:
            return f"Database error: {str(error)}"
        finally:
            connection.close()

    def updateInventoryQuantity(self, cursor, itemID, quantity):
        cursor.execute("SELECT Quantity FROM Inventory WHERE ItemID=?", (itemID,))
        result = cursor.fetchone()

        if not result:
            return "item not found"

        currentQuantity = result[0]
        newQuantity = currentQuantity - quantity

        if newQuantity == 0:
            cursor.execute("DELETE FROM Inventory WHERE ItemID=?", (itemID,))
        else:
            cursor.execute("UPDATE Inventory SET Quantity=? WHERE ItemID=?", (newQuantity, itemID))
        return "success"

    def checkout(self, accountID: int):
        connection = None
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()
            
            # First, get all items from cart with their quantities
            cursor.execute("""
                SELECT ItemID, ItemName, Quantity
                FROM Cart
                WHERE AccountID = ?
            """, (accountID,))
            
            cart_items = cursor.fetchall()
            if not cart_items:
                return "Cart is empty"

            # Calculate total
            cursor.execute("""
                SELECT SUM(Price * Quantity)
                FROM Cart
                WHERE AccountID = ?
            """, (accountID,))
            
            total = cursor.fetchone()[0]
            
            # Check inventory availability for all items
            for item in cart_items:
                itemID, _, quantity = item
                cursor.execute("SELECT Quantity FROM Inventory WHERE ItemID = ?", (itemID,))
                available_quantity = cursor.fetchone()
                
                if not available_quantity or available_quantity[0] < quantity:
                    return f"Insufficient stock for item {itemID}"

            # Create order
            orderID = random.randint(100000, 999999)
            cursor.execute("""
                INSERT INTO Orders (OrderID, AccountID, OrderDate, AmountTotal)
                VALUES (?, ?, ?, ?)
            """, (orderID, accountID, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), total))
            
            # Move items from cart to order items
            cursor.execute("""
                INSERT INTO OrderItems (OrderID, ItemID, ItemName, Quantity)
                SELECT ?, ItemID, ItemName, Quantity
                FROM Cart
                WHERE AccountID = ?
            """, (orderID, accountID))
            
            # Update inventory quantities using internal method
            for item in cart_items:
                itemID, _, quantity = item
                result = self.updateInventoryQuantity(cursor, itemID, quantity)
                if result == "item not found":
                    connection.rollback()
                    return f"Error updating inventory for item {itemID}"
            
            # Clear cart
            cursor.execute("DELETE FROM Cart WHERE AccountID = ?", (accountID,))
            
            connection.commit()
            return {"orderID": orderID, "message": "Checkout successful"}
            
        except sqlite3.Error as error:
            if connection:
                connection.rollback()
            return f"Checkout failed: {str(error)}"
        finally:
            if connection:
                connection.close()