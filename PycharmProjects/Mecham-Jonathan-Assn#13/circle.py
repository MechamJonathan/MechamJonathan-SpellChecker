import turtle

class Circle:
    def __init__(self):
        self.__circle = True
        self.colors = ["red", "blue", "green", "yellow"]

    def userInput(self):
        self.startX = eval(input("enter starting X coordinate:"))
        self.startY = eval(input("enter starting Y coordinate:"))
        self.radius = eval(input("enter radius:"))
        self.color =  eval(input("what color? 1)red 2)blue 3)green 4)yellow:"))


    def draw(self):
            turtle.penup()
            turtle.goto (self.startX, self.startY)
            turtle.color(self.colors[self.color - 1])
            turtle.pendown()
            turtle.circle (self.radius)
            turtle.penup ()

