import turtle

#prompt user to input points
x1, y1 = eval(input("enter x1 and y1 for point 1:"))
x2, y2 = eval(input("enter x2 and y2 for point 2:"))

#compute the distance

distance = ((x1 - x2) * (x1 - x2) + (y1-y2) * (y1-y2)) ** 0.5

#dispaly two points and line connecting them
turtle.penup ()
turtle.goto (x1, y1) # move to (x1,y1)
turtle.pendown ()
turtle.write ("point 1")
turtle.goto (x2, y2) #move to (x2, y2)
turtle.write ("point 2")

#move to the center of line
turtle.penup ()
turtle.goto ((x1 +x2) / 2, (y1 + y2) / 2)
turtle.write (distance)

turtle.done ()