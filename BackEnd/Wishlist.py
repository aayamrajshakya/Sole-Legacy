import sqlite3
import sys

class Wishlist:
    def __init__(self):
        self.databaseName = "StoreDatabase.db"

        try:
            self.connection = sqlite3.connect(self.databaseName)
            self.cursor = self.connection.cursor()

        except sqlite3.Error as error:
            print(f"ERROR: {error}")
            sys.exit()

    def addtoWishlist(self, AccountID, ItemID):
        # fetch the item details from inventory first
        try:
            self.cursor.execute("SELECT ItemName, Brand, Price, Color, Size FROM Inventory WHERE ItemID=?", (ItemID,))
            item = self.cursor.fetchone()

            # item fetched returns a list in the form [name, brand, price, color, size], w/ each element having its own index. Indexing
            # will come into play below

            # now insert them in wishlist table
            self.cursor.execute("INSERT INTO Wishlist(AccountID, ItemId, ItemName, Brand, Price, Color, Size) VALUES (?, ?, ?, ?, ?, ?, ?)", AccountID, ItemID, item[0], item[1], item[2], item[3], item[4])
            self.connection.commit()
        
        except sqlite3.IntegrityError:
            raise Exception(f"A product with item id {ItemID} already exists")
    
    def removefromWishlist(self, AccountID, ItemID):
        try:
            self.cursor.execute("DELETE FROM Wishlist WHERE AccountID=? AND ItemID=?", (AccountID, ItemID))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                print(f"Successfully removed item {ItemID}")
            else:
                print(f"Item {ItemID}not found")
        
        except sqlite3.Error as error:
            print(f"ERROR: {error}")


    def fetchWishlist(self, AccountID):
        try:
            self.cursor.execute("SELECT ItemID, ItemName, Brand, Price, Color, Size FROM Wishlist WHERE AccountID=?", (AccountID,))
            wholeWishlist = self.cursor.fetchall()

            if not wholeWishlist:
                print("Wishlist is empty")
                return []
            
            items=[]
            for indivItem in wholeWishlist:
                ItemID, ItemName, Brand, Price, Color, Size = indivItem
                items.append((ItemID, ItemName, Brand, Price, Color, Size))

            return items
        
        except sqlite3.Error as error:
            print(f"ERROR: {error}")