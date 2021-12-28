import turtle

class Rectangle:
    def __init__(self):
        self.__rectangle = True
        self.colors = ["red", "blue", "green", "yellow"]

    def userInput(self):
        self.startX = eval(input("enter starting X coordinate:"))
        self.startY = eval(input("enter starting Y coordinate:"))
        self.height = eval(input("enter height:"))
        self.width = eval(input("enter width:"))
        self.color =  eval(input("what color? 1)red 2)blue 3)green 4)yellow:"))


    def draw(self):
        turtle.penup()
        turtle.goto (self.startX, self.startY)
        turtle.pendown()
        turtle.color(self.colors[self.color -1])
        for i in range(2):
            turtle.forward (self.height)
            turtle.left(90)
            turtle.forward (self.width)
            turtle.left(90)