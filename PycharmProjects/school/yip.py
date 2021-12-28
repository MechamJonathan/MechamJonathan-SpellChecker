import sys
value = input("enter a number:")

if not value.isdigit ():
    value = eval(value)
    sys.exit()
