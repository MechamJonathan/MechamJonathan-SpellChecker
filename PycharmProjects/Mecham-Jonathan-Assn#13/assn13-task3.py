#Jonathan Mecham
#Comp Science 1400
# program takes inputs of multiple rectangles and circles, then draws them in turtle




import turtle
from circle import Circle
from rectangle import Rectangle

def main():

    shapes = []


    menu = True
    while menu == True:
        print('''
            1) Enter Circle
            2) Enter Rectangle
            3) Remove Shape
            4) Draw Shapes
            5) Exit
            ''')
        user = eval(input("What would you like to do?:"))
        if user == 1:
            c = Circle()
            c.userInput()
            shapes.append(c)

        if user == 2:
            r = Rectangle()
            r.userInput()
            shapes.append(r)

        if user == 3:
            print("Out of", len(shapes), "shapes,")
            drop = eval(input("Which object would you like to remove?:"))
            shapes.pop(drop - 1)

        if user == 4:
            turtle.clear()
            for x in shapes:
                x.draw()

        if user == 5:
                menu = False


main()

