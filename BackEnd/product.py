import sqlite3
import sys

class Product:
    def __init__(self, itemId: int, itemName: str, description: str, image: str, url: str, quantity: int, color:str, size: str, price: float, gender: str):
        self.itemId = itemId
        self.itemName = itemName
        self.description = description
        self.image = image
        self.url = url
        self.quantity = quantity
        self.price = price
        self.gender = gender

    def getDetails(self) -> str:
        return (
            f"Item ID: {self.itemId}"
            f"Item Name: {self.itemName}"
            f"Description: {self.description}"
            f"Image: {self.image}"
            f"Url: {self.url}"
            f"Quantity: {self.quantity}"
            f"Price: {self.price:.2f}"
            f"Gender: {self.gender}"
        )