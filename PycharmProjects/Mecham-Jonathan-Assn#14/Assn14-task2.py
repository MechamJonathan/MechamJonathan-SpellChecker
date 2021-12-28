
# Jonathan Mecham
# Comp Science 1400
# Assn14 Task 2

def main():


    usersInputs = []

    run = True

    while run:
        number = input("enter a number:")
        if number.isdigit():
            usersInputs.append(number)
        if number == "":
            run = False

    numbers = [int(i) for i in usersInputs]

    def sumNumbers():
        sum = 0
        for x in numbers:
            sum += x
        return sum


    print("number of values entered:", len(usersInputs))
    print("max value:", max(numbers))
    print("min value:", min(numbers))
    print("sum of numbers:", sumNumbers())
    print("average value:", sumNumbers() // len(numbers))

main()
