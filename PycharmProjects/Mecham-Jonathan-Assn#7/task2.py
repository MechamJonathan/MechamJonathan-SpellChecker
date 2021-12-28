#Jonathan Mecham
#A01854679
#Comp Science 1400
#program allows user to enter two circle's coordinates and radius, and then determines if they overlap


#circle 1's inputs
x1, y1, rad1 = eval(input("Enter circle 1's center coordinates, and radius (x,y,radius):"))

#circle 2's inputs
x2, y2, rad2 = eval(input("Enter circle 2's center coordinuts, and radius (x,y,radius):"))

import math

#calculate distance between centers

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 )

if distance <= abs(rad1 - rad2):
    print("Circle 2 is inside circle 1.")

elif distance <= rad1 + rad2:
    print ("Circle 2 overlaps circle 1.")

else:
    print ("Circle 2 does not overlap.")


