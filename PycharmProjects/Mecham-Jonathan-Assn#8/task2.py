# Jonathan Mecham
# A01854679
# Comp Science 1400
# Three doors, one with a car, two with goats. Pick your first door or switch.
# System places game 100,000 times and calculates your winning and losing percentages


win = 0
lose = 0
replay = 1

import random

x = eval(input("Enter 1 to stay, or 0 to switch:"))

while replay == 1:
    for i in range (1,100000):
        car = random.randint (1,3)
        usersPick = random.randint (1,3)

        #stay
        if x == 1:
            if car == usersPick:
                win += 1
            else:
                lose += 1

        #switch
        if x == 0:
            if car == usersPick:
                lose +=1
            else:
                win +=1


    print ("winning %:", str(int((win / 100000) * 100)))
    print ("losing %:", str(int((lose / 100000) * 100)))

    answer = input("Would you like to play again? (Y,N):")

    if answer == "Y":
        replay = 1
        win = 0
        lose = 0

    else:
        replay = 0

print ("Thanks for playing!")
