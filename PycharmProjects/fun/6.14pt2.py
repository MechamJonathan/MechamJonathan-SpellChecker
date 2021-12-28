import turtle
from UsefulTurtleFunctions import *


#draw line from (-50, -50) to (50, 50)
drawLine(-50, -50, 50, 50)

#write text at (-50, -60)
writeText("Testing usefule turtle functions", -50, -60)

#draw a point at (0,0)

drawPoint (0,0)

#draw a circle at (0,0 with radius 80
drawCircle( 0, 0, 80)

#draw a rectangle at (0,0) with width 60 and height 40
drawRectangle(0, 0, 60, 40)

turtle.hideturtle ()
turtle.done ()