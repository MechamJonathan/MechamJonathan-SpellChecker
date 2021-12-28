
import turtle

#draw line from (x1, y1) to (x2, y2)
def drawLine (x1, y1, x2, y2):
    turtle.penup ()
    turtle.goto (x1,y1)
    turtle.pendown ()
    turtle.goto (x2, y2)

#write a string s at the specifide location
def writeText (s, x, y):
    turtle.penup ()
    turtle.goto (x,y)
    turtle.pendown ()
    turtle.write (s)

#draw a point at the specified location (x,y)
def drawPoint (x, y):
    turtle.penup ()
    turtle.goto(x,y)
    turtle.pendown ()
    turtle.begin_fill ()
    turtle.circle (3)
    turtle.end_fill ()

#draw a circle centered at (x,y) with the specified radius
def drawCircle (x = 0, y = 0, radius = 10) :
    turtle.penup ()
    turtle.goto (x, y - radius)
    turtle.pendown ()
    turtle.circle (radius)

#draaw a rectangle at (x,y) with the specified width and height
def drawRectangle (x = 0, y = 0, width = 10, height = 10) :
    turtle.penup()
    turtle.goto (x + width / 2, y + height / 2)
    turtle.pendown ()
    turtle.right (90)
    turtle.forward (height)
    turtle.right (90)
    turtle.forward (width)
    turtle.right (90)
    turtle.forward (height)
    turtle.right (90)
    turtle.forward (width)
