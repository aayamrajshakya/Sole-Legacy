import sqlite3
import sys

class Product:
    def __init__(self, name: str, description: str, price: float, stockQuantity: int, shoeSize: str, brand: str, shoeImg: str):
        self.name = name
        self.description = description
        self.price = price
        self.stockQuantity = stockQuantity
        self.shoeSize = shoeSize
        self.brand = brand
        self.shoeImg = shoeImg  # Add an attribute for the shoe image file path

    def getDetails(self) -> str:
        # Returns a formatted string of product details
        return (
            f"Product Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Price: ${self.price:.2f}\n"
            f"Stock Quantity: {self.stockQuantity}\n"
            f"Shoe Size: {self.shoeSize}\n"
            f"Brand: {self.brand}"
        )