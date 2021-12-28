# Jonathan Mecham
# A01854679
# comp science 1400
# Task 2 Excercise 3.9

name = (input ("enter employees name:"))
hoursWorked = eval(input("Enter number of hours worked:"))
hourlyRate = eval(input( "Enter hourly pay rate:"))
federalTax = eval(input("Enter federal tax withholding rate (ex. 0.12):"))
stateTax = eval(input("Enter state tax withholding rate (ex.0.6):"))

grossPay = hoursWorked * hourlyRate
fedDeduction = grossPay * federalTax
staDeduction = grossPay * stateTax
totalDeduction = fedDeduction + staDeduction
netPay = grossPay - totalDeduction

print ()
print(format(name.upper() + "PAY INFORMATION", "^40"))

print ()
print(format("Pay", "^40"))
print(format("Hours worked:", ">29") + format(hoursWorked, "10.2f"))
print(format("Pay Rate:", ">29") + format(hourlyRate, "10.2f"))
print(format("Gross Pay:", ">29") + format(grossPay, "10.2f"))

print ()
print (format("Deductions", "^40"))
print (format("Federal Withholding(" + str(federalTax) + "%):", ">29") + "$" + format(fedDeduction, "9.2f"))
print (format("State Withholding (" + str(stateTax) +"%):", ">29") + "$" + format(staDeduction, "9.2f"))
print (format("Total Deduction:", ">29") + "$" +format (totalDeduction, "9.2f"))

print ()
print(format("Net Pay:", ">29") + "$" + format(netPay, "9.2f"))