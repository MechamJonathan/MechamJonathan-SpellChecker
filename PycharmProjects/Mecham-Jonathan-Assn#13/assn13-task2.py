#Jonathan Mecham
#Comp Science 1400
# Program generates 1000 random numbers between 0-9, then tells you how many of each number there are in the list.


import random

def main():

    counts = [0,1,2,3,4,5,6,7,8,9]
    countList = [0]
    i = 0
    while i < 1000:
        countList.append(random.randint(0,9))
        i += 1
    print(countList)

    count = countList.count(0)
    print("0:", count)

    count = countList.count(1)
    print("1:", count)

    count = countList.count(2)
    print("2:", count)

    count = countList.count(3)
    print ("3:", count)

    count = countList.count(4)
    print("4:", count)

    count = countList.count(5)
    print("5:", count)

    count = countList.count(6)
    print("6:", count)

    count = countList.count(7)
    print("7:", count)

    count = countList.count(8)
    print("8:", count)

    count = countList.count(9)
    print("9:", count)



main()