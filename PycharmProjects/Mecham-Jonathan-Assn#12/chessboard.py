#Jonathan Mecham
#Computer Science 1400
#Assn 12 task 1
#program uses classes to draw chessboard based on user's inputs



import turtle

class Chessboard():

    def __init__(self, startX, startY, width=250, height=250):
        self.startX = startX
        self.startY = startY
        self.width = width
        self.height = height

    # outline of board
    def drawBoard(self):
        turtle.penup()
        turtle.goto(self.startX, self.startY)
        turtle.pendown()
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)

    # draw rectangle
    def drawRectangle(self):
        turtle.penup()
        turtle.goto(self.startX, self.startY)
        turtle.pendown()
        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(self.width / 8)
        turtle.left(90)
        turtle.forward(self.height / 8)
        turtle.left(90)
        turtle.forward(self.width / 8)
        turtle.left(90)
        turtle.forward(self.height / 8)
        turtle.end_fill()

    #draws all the the rectangles on the board
    def drawAllRectangles(self):
        leftRow = 0
        while leftRow <= 4:
            rectangle = 0
            self.startX, self.startY = self.startX, self.startY
            while rectangle <= 4:
                Chessboard.drawRectangle(self)
                rectangle += 1
                self.startX += (self.width / 8) * 2
                if rectangle == 4:
                    leftRow += 1
                    self.startY += (self.height / 8) * 2
                    self.startX = (self.startX - self.startX)
                    break
            if leftRow == 4:
                break
        rightRow = 0
        self.startY = self.startY - self.startY
        self.startX += self.width / 8
        self.startY += self.height / 8
        while rightRow <= 4:
            rectangle = 0
            while rectangle <= 4:
                Chessboard.drawRectangle(self)
                rectangle += 1
                self.startX += (self.width / 8) * 2
                if rectangle == 4:
                    rightRow += 1
                    self.startX = self.startX - self.startX
                    self.startX += self.width / 8
                    self.startY += (self.height / 8) * 2
                    break
            if rightRow == 4:
                break

    def draw(self):
        Chessboard.drawBoard(self)
        Chessboard.drawAllRectangles(self)

