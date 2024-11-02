import sqlite3
import sys
import string
import random

class User:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("StoreDatabase.db")
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            print(f"ERROR: {error}")
            sys.exit()
        
        self.loggedIn = False
        self.loggedAccountID = None

    def createAccount(self, fullName: str, email: str, password: str, address: str, userType: str) -> str:
        # check if account with email address exists or not
        self.cursor.execute("SELECT Email FROM UserAccounts WHERE Email=?", (email,))

        if self.cursor.fetchone():
            return "Email address in use"
        
        # Inspired by https://medium.com/@jeraldcrisb/generate-random-username-using-python-4fa31a061695
        characters = string.ascii_letters + string.digits + '._-'
        randLetters = ''.join(random.choice(characters) for _ in range(random.randint(5, 10)))
        randNumbers = str(random.randint(1,100))
        AccountID = randNumbers + randLetters

        try:
            data = (AccountID, fullName, email, password, address, userType)
            self.cursor.execute("INSERT INTO UserAccounts (AccountID, FullName, Email, Password, Address, UserType) VALUES (?, ?, ?, ?, ?, ?)", data)
            self.connection.commit()
        except sqlite3.Error as error:
            return f"Error: {error}"
    
    def loginAccount(self, email: str, password: str) -> str:
        try:
            self.cursor.execute("SELECT * FROM UserAccounts WHERE Email=? AND Password=?", (email, password))
            result = self.cursor.fetchone()

            if result is None:
                return "Login credentials didn't match"
            else:
                self.loggedIn = True
                self.loggedAccountID = result[0]
                return "successful"

        except sqlite3.Error as error:
            return f"ERROR: {error}"
        
    def logoutAccount(self):
        self.loggedAccountID = None
        self.loggedIn = False
        return "Logged out"
    
    def updateAccount(self, parameter: str, newVal: str) -> str:
        # only logged-in user can update info, so using self.loggedAccountID
        try:
            self.cursor.execute(f"UPDATE UserAccounts SET {parameter}=? WHERE AccountID=?", (newVal, self.loggedAccountID))
            self.connection.commit()
            return "successful"
        except sqlite3.Error as error:
            return f"ERROR: {error}"
    
    def deleteAccount(self, email: str) -> str:
        try:
            self.cursor.execute("DELETE FROM UserAccounts WHERE Email=?", (email,))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return "sucessful"
            else:
                return "failure"
        except sqlite3.Error as error:
            return f"ERROR: {error}"
        
def __del__(self):
    self.cursor.close()
    self.connection.commit()
    self.connection.close()