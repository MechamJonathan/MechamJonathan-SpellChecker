# Jonathan Mecham
# Comp Science
# Assn 5 task 2
# program allows user to enter custom inputs to create a archery target

center_location = eval(input("enter center x,y location of target:"))

radius = eval(input("enter bullseye radius:"))

first_ring = radius + 25

second_ring = first_ring + 25

third_ring = second_ring + 25

import turtle

#third ring
turtle.penup ()
turtle.color ("red")
turtle.goto (center_location)
turtle.forward (third_ring)
turtle.right (270)
turtle.begin_fill ()
turtle.pendown ()
turtle.circle (third_ring)
turtle.end_fill ()
turtle.penup()

#second ring
turtle.color ("blue")
turtle.goto (center_location)
turtle.forward (second_ring)
turtle.right (270)
turtle.begin_fill ()
turtle.pendown ()
turtle.circle (second_ring)
turtle.end_fill ()
turtle.penup ()

#third_ring
turtle.color ("yellow")
turtle.goto (center_location)
turtle.forward (first_ring)
turtle.right (270)
turtle.pendown ()
turtle.begin_fill ()
turtle.circle (first_ring)
turtle.end_fill ()
turtle.penup ()

#bullseye
turtle.color ("black")
turtle.penup ()
turtle.goto (center_location)
turtle.forward (radius)
turtle.right (270)
turtle.pendown ()
turtle.begin_fill ()
turtle.circle (radius)
turtle.end_fill ()
turtle.penup ()

turtle.hideturtle ()
turtle.done ()