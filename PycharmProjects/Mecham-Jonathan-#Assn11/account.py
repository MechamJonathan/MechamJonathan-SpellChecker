#Jonathan Mecham
#Comp Science 1400
# program that takes input from user and outputs bank statement



class Account:

    def __init__(self):
        self.__id = True
        self.__balance = True
        self.__interest = True

    def userInput(self):
        self.__accountId = eval(input("Please enter account ID:"))
        self.__accountBalance = eval(input("Please enter account balance:"))
        self.__annualInterestRate = eval(input("please enter annual interest rate:"))

    def userAccountId(self):
        return self.__accountId

    def userAccountBalance(self):
        return self.__accountBalance

    def userAnnualInterestRate(self):
        return self.__annualInterestRate

    def monthlyInterestRate (self):
        monthlyInterestRate = round((((self.__annualInterestRate/ 100) / 12) *100), 2)
        print ("$", monthlyInterestRate)

    def monthlyInterest (self):
        monthlyInterestAm = round(self.__accountBalance * ((self.__annualInterestRate / 12) / 100), 2)
        print ("$", monthlyInterestAm)

    def setWithdraw(self):
        self.withdraw = eval(input("Enter a withdrawl ammount: "))
        self.__accountBalance = self.__accountBalance - self.withdraw

    def setDeposit(self):
        self.deposit = eval(input("Enter a deposit amount: "))
        self.__accountBalance = self.__accountBalance + self.deposit

def main():

    menu = Account()
    menu.userInput()
    done = False

    while not done:

        print ("Account ID:", menu.userAccountId())
        print ("Account balance $:", menu.userAccountBalance())
        print("Annual interest rate: $", menu.userAnnualInterestRate())
        menu.monthlyInterestRate()
        menu.monthlyInterest()
        print("what would you like to do?")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Exit")

        response = eval(input("Make a selection:"))

        if response == 1:
            menu.setWithdraw()
        elif response == 2:
            menu.setDeposit()
        elif response == 3:
            break

    print ("Thank you")

main()