


x1, y1 = eval(input("enter point 1 (x,y):"))

x2, y2 = eval(input("enter point 2 (x,y):"))

import math
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

distanceX = abs(x2 - x1)
distanceY = abs(y2 - y1)

print("Distance in x direction:", distanceX)
print("Distance in y direction:", distanceY)
print ("the total distance between the points is: ", distance)