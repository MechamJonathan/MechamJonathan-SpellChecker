
#Jonathan Mecham
#Comp science 1400
#Assn 12 Task 2
#program validates user's password

from password import Password
import sys

def main():
    p = Password()
    runAgain = "Y"

    while runAgain == "Y":
        password = input("Enter a password:")
        p.setString(password)
        p.isValid(password)
        p.getErrorMessage(password)

        print()
        print ("Would you like to test another password?")
        runAgain = input("Enter Y or N:")

    if runAgain == "N":
        sys.exit()

main()
