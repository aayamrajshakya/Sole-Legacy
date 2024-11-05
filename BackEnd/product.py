import sqlite3
import sys

class Product:
    def __init__(self, itemId: int, brand: str, itemName: str, description: str, image: str, quantity: int, color:str, size: str, price: float, gender: str):
        self.itemId = itemId
        self.brand = brand
        self.itemName = itemName
        self.description = description
        self.image = image
        self.quantity = quantity
        self.color = color
        self.size = size
        self.price = price
        self.gender = gender

    def getDetails(self) -> str:
        return (
            f"Item ID: {self.itemId}"
            f"Brand: {self.brand}"
            f"Item Name: {self.itemName}"
            f"Description: {self.description}"
            f"Quantity: {self.quantity}"
            f"Color: {self.color}"
            f"Size: {self.size}"
            f"Price: {self.price:.2f}"
            f"Gender: {self.gender}"
        )