# Jonathan Mecham
# a01854679
# Comp Science 1400
# system tests numbers and finds 4 perfect numbers between 1-10,000



perfectNumbers = 0
count = 0

import sys

for x in range(2,10000):
    sum = 0

    for i in range (1, (x //2) + 1):
        count += 1
        if x % i == 0:
            factor = i
            sum += factor


    if sum == x:
        print (x)
        perfectNumbers += 1

    if perfectNumbers == 4:
        print ("system run time:", count)
        sys.exit ()
