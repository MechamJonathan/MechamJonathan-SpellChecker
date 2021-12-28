#Jonathan Mecham
# A01854679
# Computer Science 1400
# Assn 6 task 1 Excercise 3.5

# This program solves for the area of a polygon based upon the inputed sides and length.


sides = (eval(input("Enter number of sides:")))
sideLength = (eval(input("Enter length of side:")))

import math

area = (sides * math.pow(sideLength, 2) / (4 * math.tan(math.pi/ sides)))



print (round(area))