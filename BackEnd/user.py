# regarding why i put `check_same_thread` arg: 
# https://thewebdev.info/2022/04/03/how-to-fix-programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-same-thread-with-python-sqlite3/

import sqlite3
import bcrypt 

class User:
    def __init__(self):
        self.loggedIn = False
        self.loggedAccountID = None
        self.connection = sqlite3.connect('StoreDatabase.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    def createAccount(self, fullName: str, email: str, plain_password: str, address: str, usertype: str) -> str:
        # check if account with email address exists or not
        self.cursor.execute("SELECT Email FROM UserAccounts WHERE Email=?", (email,))

        if self.cursor.fetchone():
            return "Email address in use"
        
        # https://peerdh.com/blogs/programming-insights/implementing-password-hashing-techniques-in-user-authentication-for-crud-applications-with-sqlite
        # https://stackoverflow.com/a/48213392/23011800
        bvalue = plain_password.encode('utf-8')
        temp_hash = bcrypt.hashpw(bvalue, bcrypt.gensalt())
        hashed_password = temp_hash.decode('utf-8')

        try:
            data = (fullName, email, hashed_password, address, usertype)
            self.cursor.execute("INSERT INTO UserAccounts (FullName, Email, Password, Address, UserType) VALUES (?, ?, ?, ?, ?)", data)
            self.connection.commit()
            return "successful"
        except sqlite3.Error as error:
            return f"Error: {error}"
    
    def loginAccount(self, email: str, plain_password: str) -> str:
        try:
            self.cursor.execute("SELECT * FROM UserAccounts WHERE Email=?", (email,))
            result = self.cursor.fetchone()

            if result is None:
                return "Email address not found"
            
            hashed_password = result[3]
            if bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8')):
                self.loggedIn = True
                self.loggedAccountID = result[0]
                return "successful"
        
            else:
                return "Login credentials don't match"

        except sqlite3.Error as error:
            return f"{error}"
        
    def logoutAccount(self):
        self.loggedAccountID = None
        self.loggedIn = False
        return "successful"
    
    def updateAccount(self, parameter: str, newVal: str) -> str:
        # only logged-in user can update info
        if not self.loggedIn:
            return "must log in"
        
        try:
            self.cursor.execute(f"UPDATE UserAccounts SET {parameter}=? WHERE AccountID=?", (newVal, self.loggedAccountID))
            self.connection.commit()
            return "successful"
        except sqlite3.Error as error:
            return f"ERROR: {error}"
    
    def deleteAccount(self) -> str:
        if not self.loggedIn:
            return "must log in"
        
        try:
            self.cursor.execute("DELETE FROM UserAccounts WHERE Email=?", (self.loggedAccountID,))
            self.connection.commit()
            if self.cursor.rowcount > 0:

                # clear session after deleting the account
                self.loggedIn = False
                self.loggedAccountID = None
                return "sucessful"
            else:
                return "failure"
        except sqlite3.Error as error:
            return f"ERROR: {error}"
        