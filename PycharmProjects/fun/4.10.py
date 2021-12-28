
#system calculates how much tax you pay

import sys

#user enters filing status
status = eval(input("0 - single filer, 1 - married jointly, \n" +
                    "2 - married separately, 3 - head of houshold \n" +
                    "Enter filing status yo:"))

income = eval(input("Enter taxable income:"))

if status == 0:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = income * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = income * 0.25
    elif income <= 171550:
        tax = income * 0.28
    elif income <= 372950:
        tax = income * 0.33

elif status == 1:
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = income * 0.15
    elif income <= 137050:
        tax = income * 0.25
    elif income <= 208850:
        tax = income * 0.28
    elif income <= 372950:
        tax = income * 0.33

elif status == 2:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = income * 0.15
    elif income <= 68525:
        tax = income * 0.25
    elif income <= 104425:
        tax = income * 0.28
    elif income <= 186475:
        tax = income * 0.33

elif status == 3:
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = income * 0.15
    elif income <= 117450:
        tax = income * 0.25
    elif income <= 190200:
        tax = income * 0.28
    elif income <= 372950:
        tax = income * 0.33
    else:
        print(" you make too much money bitch")
        sys.exit()

else:
    print("invalid value.")
    sys.exit ()



print("Your tax is:", format(tax, ".2f"))