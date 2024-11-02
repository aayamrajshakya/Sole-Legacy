import sqlite3
import sys
import random


class User:
    def __init__(self):

        # Attempts to connect to the database
        try:
            self.connection = sqlite3.connect("StoreDatabase.db")

        # Exit on fail
        except sqlite3.Error:
            print("ERROR: Failed to connect to the database")
            sys.exit()

        self.cursor = self.connection.cursor()

        self.UserID: str = ""
        self.Email: str = ""
        self.Password: str = ""
        self.AccountType: str = ""
        self.LoggedIn: bool = False

    # TODO: Password encryption for secure login
    # Login Function
    def CreatAccount(self) -> None:
        FirstName: str = ""
        MiddleName: str = ""
        LastName: str = ""
        Address: str = ""
        Email: str = ""
        Password: str = ""
        UserID: str = ""
        SpecialChar: tuple = ('!', '@', '#', '$', '%', '^', '&', '*', '-', '_')

        # Verifies Email meets parameters
        while True:
            Email: str = input("What email address would you like to use?\n").lower()

            # Checks for similar email address among all accounts
            self.cursor.execute("SELECT Email FROM UserAccounts WHERE Email = ?", (Email,))
            UserResult = self.cursor.fetchall()
            self.cursor.execute("SELECT Email FROM AdminAccounts WHERE Email = ?", (Email,))
            AdminResult = self.cursor.fetchall()
            self.cursor.execute("SELECT Email FROM SellerAccounts WHERE Email = ?", (Email,))
            SellerResult = self.cursor.fetchall()

            if "@" not in Email:
                print("ERROR: That is not a valid email address format, make sure provider extension is present '@example.com' ")
                continue

            # if a result is found supply error message
            elif UserResult or AdminResult or SellerResult:
                print("ERROR: An account with this email address already exists.")
                continue

            print("Valid email address accepted.\n")
            break

        # Loop to guarantee that password parameters are met
        while True:
            Password: str = input(f"Please enter a password, Must contain at least 8 characters, and include 1 special character {SpecialChar} \n")

            # checks to ensure password is 8 or more characters
            if len(Password) < 8:
                print("ERROR: Password must be at least 8 characters\n")
                continue

            # Ensures password contains at least one of the pre-determined special characters
            elif len(Password) >= 8:
                for i in SpecialChar:
                    if i in Password:
                        break
                    else:
                        print("ERROR: Password must contain at least one of these special characters ", SpecialChar, "\n")
                        break

            # Checks for Password Verification
            while True:
                VerifyPass: str = input("Please Verify your password\n")
                if VerifyPass == Password:
                    break
                else:
                    print("Password doesn't match, please try again\n")
                    continue

            print("\nPassword Accepted!")
            print("Account Creation successful!, Welcome to Sole Legacy!\n")
            break

        # Generate User's database ID
        while True:
            for i in range(10):
                UserID += str(random.randint(0, 9))

            # Checks for similar UserID among all Databases
            self.cursor.execute("SELECT AccountID FROM UserAccounts WHERE AccountID = ?", (UserID,))
            UserResult = self.cursor.fetchall()
            self.cursor.execute("SELECT AdminID FROM AdminAccounts WHERE AdminID = ?", (UserID,))
            AdminResult = self.cursor.fetchall()
            self.cursor.execute("SELECT SellerID FROM SellerAccounts WHERE SellerID = ?", (UserID,))
            SellerResult = self.cursor.fetchall()

            # if comparison is True then will return to the beginning of the loop and resets UserID value back to NULL
            if UserResult or AdminResult or SellerResult:
                print("Account by that UserID already exists within our database!\n")
                UserID = ""
                continue
            else:
                break

        # if email specifically includes "sole-legacy" within email address add to admin database instead
        if "@sole-legacy" in Email.lower():
            try:
                self.cursor.execute("INSERT INTO AdminAccounts (AdminID, Email, Password) VALUES (?, ?, ?)", (UserID, Email, Password))
                self.connection.commit()

            except sqlite3.Error:
                print("ERROR: An error occurred while inserting into database")

            print("successfully registered Admin account.")
        else:
            FirstName: str = input("Please enter your first name\n")
            LastName: str = input("Please enter your last name\n")
            Address: str = input("Please enter your address: Format: (Road/street, Town/City & state, Zip Code)\n")

            try:
                self.cursor.execute("INSERT INTO UserAccounts (AccountID, FirstName, MiddleName, LastName, Email, Password, Address) VALUES (?, ?, ?, ?, ?, ?, ?)", (UserID, FirstName, MiddleName, LastName, Email, Password, Address))
                self.connection.commit()

            except sqlite3.Error:
                print("ERROR: An error occurred while inserting into database")

    # TODO: Password decryption for verification
    # Login function
    def Login(self, Email: str, Password: str) -> None:

        # Attempts login process
        try:

            # Retrieves Account data if it exits within the Buyer database under the entered email and password
            self.cursor.execute("SELECT * FROM UserAccounts WHERE Email=? AND Password=?", (Email.lower(), Password))
            Buyer = self.cursor.fetchall()

            # If account is found, applies relative tags to the User
            if Buyer:
                self.AccountType = "Buyer"
                self.UserID = Buyer[0][0]
                self.Email = Buyer[0][4]
                self.Password = Buyer[0][5]
                self.LoggedIn = True
                print("Buyer successfully logged in")

            # Retrieves Account data if it exits within the Admin database under the entered email and password
            self.cursor.execute("SELECT * FROM AdminAccounts WHERE Email=? AND Password=?", (Email.lower(), Password))
            Admin = self.cursor.fetchall()

            # If account is found, applies relative tags to the User
            if Admin:
                self.AccountType = "Admin"
                self.UserID = Admin[0][0]
                self.Email = Buyer[0][1]
                self.Password = Buyer[0][2]
                self.LoggedIn = True
                print("Admin successfully logged in")

            # Retrieves Account data if it exits within the Seller database under the entered email and password
            self.cursor.execute("SELECT * FROM SellerAccounts WHERE Email=? AND Password=?", (Email.lower(), Password))
            Seller = self.cursor.fetchall()

            # If account is found, applies relative tags to the User
            if Seller:
                self.AccountType = "Seller"
                self.UserID = Buyer[0][0]
                self.Email = Buyer[0][1]
                self.Password = Buyer[0][2]
                self.LoggedIn = True
                print("Seller successfully logged in")

            # If Account isn't found within any of the account databases raise an exception
            if not Buyer and not Admin and not Seller:
                raise Exception()

        # Appears when exception is raised
        except Exception as e:
            print("ERROR: Account doesn't exist within our database.\n")

    def Logout(self) -> None:
        self.LoggedIn = False
        sys.exit()

    def UpdateAccountInfo(self):
        count: int = 0

        if self.AccountType == "Buyer" or "Seller":
            InfoSection: str = input("""What info would you like to change?\n
                                    1) Account Name\n
                                    2) Email\n
                                    3) Password\n
                                    4) Address Information\n""")

            # Change account name
            if InfoSection == "1":
                NewName = input("Please enter your new name, format(first, middle, last)\n"
                                "NOTE: must include ',' to separate words.\n"
                                "NOTE: if you would like to remove your middle name, please enter '-' as a place holder.\n")
                NameList: list = []

                for i in NewName.split(','):
                    NameList.append(i.strip())

                for i in range(len(NameList)):
                    if NameList[i] == "":
                        continue

                    try:
                        if NameList[i] == "-" and i == 1:
                            self.cursor.execute("UPDATE UserAccounts SET MiddleName='' WHERE AccountID=?", (self.UserID,))
                            self.connection.commit()
                            continue

                        if i == 0:
                            self.cursor.execute("UPDATE UserAccounts SET FirstName=? WHERE AccountID=?", (NameList[i], self.UserID))
                            self.connection.commit()

                        elif i == 1:
                            self.cursor.execute("UPDATE UserAccounts SET MiddleName=? WHERE AccountID=?", (NameList[i], self.UserID))
                            self.connection.commit()

                        elif i == 2:
                            self.cursor.execute("UPDATE UserAccounts SET LastName=? WHERE AccountID=?", (NameList[i], self.UserID))
                            self.connection.commit()

                    except sqlite3.Error:
                        print("ERROR: An error occurred while updating your name.\n")

            # Change Email
            if InfoSection == "2":
                Email: str
                while True:
                    Email: str = input("What email address would you like to use?\n").lower()

                    # Checks for similar email address among all accounts
                    self.cursor.execute("SELECT Email FROM UserAccounts WHERE Email = ?", (Email,))
                    UserResult = self.cursor.fetchall()
                    self.cursor.execute("SELECT Email FROM AdminAccounts WHERE Email = ?", (Email,))
                    AdminResult = self.cursor.fetchall()
                    self.cursor.execute("SELECT Email FROM SellerAccounts WHERE Email = ?", (Email,))
                    SellerResult = self.cursor.fetchall()

                    if "@" not in Email:
                        print("ERROR: That is not a valid email address format, make sure provider extension is present '@example.com' ")
                        continue

                    # if a result is found supply error message
                    elif UserResult or AdminResult or SellerResult:
                        print("ERROR: An account with this email address already exists.")
                        continue

                    print("Valid email address accepted.\n")
                    break

                try:
                    # changes the email address for relevant account type
                    if self.AccountType == "Buyer":
                        self.cursor.execute("UPDATE UserAccounts SET Email=? WHERE AccountID=?", (Email, self.UserID))
                        self.connection.commit()

                    elif self.AccountType == "Seller":
                        self.cursor.execute("UPDATE SellerAccounts SET Email=? WHERE SellerID=?", (Email, self.UserID))
                        self.connection.commit()

                except sqlite3.Error as error:
                    print("ERROR: There was an issue with updating your email.\n")

            # TODO: Password encryption and decryption
            # Change Password
            if InfoSection == "3":
                SpecialChar: tuple = ('!', '@', '#', '$', '%', '^', '&', '*', '-', '_')

                # Loop to guarantee that password parameters are met
                while True:
                    Password: str = input(f"Please enter a password, Must contain at least 8 characters, and include 1 special character {SpecialChar} \n")

                    # checks to ensure password is 8 or more characters
                    if len(Password) < 8:
                        print("ERROR: Password must be at least 8 characters\n")
                        continue

                    # Ensures password contains at least one of the pre-determined special characters
                    elif len(Password) >= 8:
                        for i in SpecialChar:
                            if i in Password:
                                break
                            else:
                                print("ERROR: Password must contain at least one of these special characters ", SpecialChar, "\n")
                                break

                    try:
                        if self.AccountType == "Buyer":
                            self.cursor.execute("UPDATE UserAccounts SET Password=? WHERE AccountID=?", (Password, self.UserID))
                            self.connection.commit()

                        elif self.AccountType == "Seller":
                            self.cursor.execute("UPDATE SellerAccounts SET Password=? WHERE SellerID=?", (Password, self.UserID))
                            self.connection.commit()

                    except sqlite3.Error as error:
                        print("ERROR: There was an issue with updating your password.\n")

                if InfoSection == "4":
                    Address: str = input("Please enter your address: Format: (Road/street, Town/City & state, Zip Code)\n")

                    self.cursor.execute("UPDATE UserAccounts SET Address=? WHERE AccountID=?", (Address, self.UserID))
                    self.connection.commit()

    def DeleteAccount(self):
        Email = input("What email address of the account you would you like to delete?\n").lower()
        Password: str = input("Please enter your password: \n")

        # Checks for Password Verification
        while True:
            VerifyPass: str = input("Please Verify your password\n")
            if VerifyPass == Password:
                break
            else:
                print("Password doesn't match, please try again\n")
                continue

        try:
            self.cursor.execute("DELETE FROM UserAccounts WHERE AccountID=?", (self.UserID,))
            self.connection.commit()

        except sqlite3.Error as error:
            print("ERROR: Failed to remove information from the database.\n")

        print("Account successfully deleted, GoodBye.\n")

    # De-constructor 
    def __del_(self):
        self.cursor.close()
        self.connection.close()