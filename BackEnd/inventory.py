import sqlite3
import random

class Inventory:

    # Class Initializer
    def __init__(self):
        self.databaseName = "StoreDatabase.db"

        # Attempts Database connection
        try:
            self.connection = sqlite3.connect(self.databaseName)
            self.cursor = self.connection.cursor()

        # If connection fails raises error and exits program
        except sqlite3.Error as error:
             return f"{error}"


    # Function for Adding Items to the Inventory database
    def AddProduct(self, Brand: str, ItemName: str, Description: str, Image: str, Quantity: int, Color: str, Size: str, Price: str, Gender: str) -> None:
        
        ### https://www.w3schools.com/python/ref_random_randint.asp
        ItemID = str(random.randint(10000000, 99999999))

        # Tries initial Query to add the item to the database
        try:
            self.cursor.execute("INSERT INTO Inventory (ItemID, Brand, ItemName, Description, Image, Quantity, Color, Size, Price, Gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (ItemID, Brand, ItemName, Description, Image, Quantity, Color, Size, Price, Gender))
            self.connection.commit()

        ### https://stackoverflow.com/questions/36518628/sqlite3-integrityerror-unique-constraint-failed-when-inserting-a-value
        # If the item already exists then will raise an error
        except sqlite3.IntegrityError as error:
            return f"{error}"

    def RemoveProduct(self, ItemID: str) -> None:
        self.cursor.execute("SELECT * FROM Inventory WHERE ItemID=?", (ItemID,))
        result = self.cursor.fetchall()

        # If the ItemID doesn't exist then raise exception for error checking
        if not result:
            raise Exception(f"The item by the ID {ItemID} was not found\n")

        else:
            self.cursor.execute("DELETE FROM Inventory WHERE ItemID=?", (ItemID,))
            self.connection.commit()
            return "successfully deleted"

    # Function of updating database item quantities
    def UpdateStockQuantity(self, ItemID: str, Quantity: int, AddOrRemove: bool) -> None:

        # Initial query to grab the quantity of the item with the proper item ID
        self.cursor.execute("SELECT Quantity FROM Inventory WHERE ItemID=?", (ItemID,))
        result = self.cursor.fetchone()

        if not result:
            return "item not found"

        # fetchone gives us the quantity only; this removes the need to select the first element
        # of the first row as we had to do when fetchall was used
        currentQuantity = result[0]

        # If AddOrRemove is true, then add; if false, remove
        if AddOrRemove:
                     newQuantity = currentQuantity + Quantity
        else:
             newQuantity = currentQuantity - Quantity

             # if the updated quantity becomes 0, just remove it from the inventory
             if newQuantity == 0:
                  self.RemoveProduct(ItemID)

        self.cursor.execute("UPDATE Inventory SET Quantity=? WHERE ItemID=?", (newQuantity, ItemID))
        self.connection.commit()


    ### https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html        
    # De-constructor to ensure closing of connections
    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()