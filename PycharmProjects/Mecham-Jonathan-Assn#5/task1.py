# Jonathan Mecham
# A01854679
# Comp Science
# Assn 5 task 1

investmentAmount = eval(input("Enter investment amount:"))
monthlyInterestRate = eval(input("Enter annual interest rate:"))
numberOfYears = eval(input("enter number of years:"))

adjustedMonthlyInterestRate = monthlyInterestRate / 100 / 12
numberOfMonths = (numberOfYears * 12)

futureInvestmentValue = investmentAmount * ((1 + adjustedMonthlyInterestRate) ** numberOfMonths)

print ("Accumulated value is ", futureInvestmentValue)

print (adjustedMonthlyInterestRate)
print (numberOfMonths)