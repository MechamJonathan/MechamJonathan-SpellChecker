#Jonathan Mecham
#Comp science 1400
#Assn 12 Task 2
#program validates user's password


import sys


class Password:

    def __init__(self, password = "password"):
        self.string = password

    def getString(self):
        return self

    def setString(self, password):
        self.string = password

    def __islength(self,password):
        if len(password) > 8:
            return True

    def __isTwoDigits(self,password):
        if not len([x for x in password if x.isdigit()]) < 2:
            return True

    def __isEnding123(self, password):
        if not (password[len(password) - 1] == "3" and \
                password[len(password) - 2] == "2" and \
                password[len(password) - 3] == "1"):
            return True

    def __isPassword(self,password):
        if not "password" in password:
            return True

    def __isAlphaNum(self, password):
        if password.isalnum():
            return True

    def isValid(self, password):
        if Password.__islength(self, password):
            if Password.__isTwoDigits(self, password):
                if Password.__isEnding123(self, password):
                    if Password.__isPassword(self, password):
                        if Password.__isAlphaNum(self, password):
                            print("Password is valid!:)")

    def getErrorMessage(self, password):
        if not Password.__islength(self, password):
            print("password must be 8 characters long")
        if not Password.__isTwoDigits(self, password):
            print("password must contain atleast two digits")
        if not Password.__isEnding123(self, password):
            print ("password cannot end in 123")
        if not Password.__isPassword(self, password):
            print ("password cannot have the word password in it")
        if not Password.__isAlphaNum(self, password):
            print ("password must ONLY contain letters and digits")


