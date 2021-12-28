#let the user enter interest rate, loan amount, number of year.
#Display monthly payment, total of all payments.

# " system analysis
#     formulas
#         monthly payment = loan amount x monthly interest rate / (1-1/(1+ monthly interest rate) ^num of months)
#           montly interest rate = annual interest rate / 12
#           total payments = monthly payment * 12 * num of years

#system design
#   prompt the user to enter
#       interest rate (annual, xx.xx%)
#       loan amount
#        number of years
#convert interest
#       interest as a decimal xx.xx% to 0.xxx
#       monthly interest rate. annual rate / 12
#        together- annual interest / 1200
# compute
#   monthly payment
#   total payments
#   Display shiz


annualInterestRate = eval(input("Enter the loan rate. ex 8.35:"))
loanAmount = eval(input("Enter a loan amount:"))
