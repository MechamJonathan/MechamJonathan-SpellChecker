#Jonathan Mecham
#A01854679
#Comp Science 1400
# Chessboard. Program takes inputs of location, length, and height and prints a chessboard.



import turtle

# outline of board
def drawBoard (startX, startY, length, height):
    turtle.penup()
    turtle.goto (startX, startY)
    turtle.pendown()
    turtle.forward (length)
    turtle.left (90)
    turtle.forward (height)
    turtle.left (90)
    turtle. forward (length)
    turtle. left (90)
    turtle. forward (height)

#draw rectangle
def drawRectangle(startX, startY, length, height):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(length / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.left(90)
    turtle.forward(length / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.end_fill()

#draws all the the rectangles on the board
def drawAllRectangles(startX, startY, length=250, height=250):
    leftRow = 0
    while leftRow <= 4:
        rectangle = 0
        startX, startY = startX, startY
        while rectangle <= 4:
            drawRectangle(startX, startY, length, height)
            rectangle += 1
            startX += (length / 8) * 2
            if rectangle == 4:
                leftRow += 1
                startY += (height / 8) * 2
                startX = (startX - startX)
                break
        if leftRow == 4:
            break
    rightRow = 0
    startY = startY - startY
    startX += length / 8
    startY += height / 8
    while rightRow <= 4:
        rectangle = 0
        while rectangle <= 4:
            drawRectangle(startX, startY, length, height)
            rectangle += 1
            startX += (length / 8) * 2
            if rectangle == 4:
                rightRow += 1
                startX = startX - startX
                startX += length / 8
                startY += (height / 8) * 2
                break
        if rightRow == 4:
            break

#runs the whole program
def main():
    import turtle

    startX, startY = eval(input("Enter beggining (x,y) location:"))
    length, height = eval(input ("Enter the length and height (length,height):"))

    if length == "" and height == "":
        drawBoard(startX, startY, length, height)
    elif height == "":
        drawBoard(startX, startY, length, height)
    elif length == "":
        drawBoard(startX, startY, length, height)
    else:
        drawBoard(startX, startY, length, height)

    drawAllRectangles(startX, startY, length, height)

    turtle.hideturtle ()
    turtle.done ()