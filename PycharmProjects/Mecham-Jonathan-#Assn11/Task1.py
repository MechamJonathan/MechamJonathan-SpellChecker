#Jonathan Mecham
#Comp Science 1400
# program creates customizable smiley face



import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True

    def __draw_head (self):
        if self.__happy == True:
        #head yellow
            turtle.speed(0)
            turtle.showturtle()
            turtle.penup()
            turtle.goto(0,-50)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("yellow")
            turtle.circle (100)
            turtle.end_fill()

        else:
            turtle.speed (0)
            turtle.showturtle ()
            turtle.penup()
            turtle.goto (0, -50)
            turtle.pendown()
            turtle.begin_fill ()
            turtle.fillcolor ("red")
            turtle.circle (100)
            turtle.end_fill ()

    def __draw_eyes (self):
        if self.__dark_eyes == True:
            #left eye (black)
            turtle.penup()
            turtle.goto (-35, 65)
            turtle.pendown ()
            turtle.begin_fill()
            turtle.fillcolor ("black")
            turtle.circle (15)
            turtle.end_fill ()

            #right eye (black)
            turtle.penup ()
            turtle.goto (35, 65)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor ("black")
            turtle.circle (15)
            turtle.end_fill()

        else:
            # left eye (blue)
            turtle.penup()
            turtle.goto(-35, 65)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.circle(15)
            turtle.end_fill()

            # right eye (blue)
            turtle.penup()
            turtle.goto(35, 65)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.circle(15)
            turtle.end_fill()

    def __draw_mouth(self):
        if self.__smile == True:
            #smile mouth
            turtle.penup()
            turtle.width(10)
            turtle.goto(-65, 15)
            turtle.setheading(315)
            turtle.pendown()
            turtle.circle(90, 90)
            turtle.penup()
            turtle.width(1)
            turtle.setheading(0)

        else:
            turtle.speed(0)
            turtle.penup()
            turtle.width(10)
            turtle.goto (65, 15)
            turtle.setheading (135)
            turtle.pendown()
            turtle.circle (90, 90)
            turtle.penup()
            turtle.width(1)
            turtle.setheading(0)


    def draw_face(self):
        turtle.clear()
        turtle.speed(0)
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def is_smile(self):
        return self.__smile

    def is_happy(self):
        return self.__happy

    def is_dark_eyes(self):
        return self.__dark_eyes

    def change_mouth(self):
        if self.__smile == True:
            self.__smile = False
        else:
            self.__smile = True
        self.draw_face()

    def change_emotion(self):
        if self.__happy == True:
            self.__happy = False
        else:
            self.__happy = True
        self.draw_face()

    def change_eyes(self):
        if self.__dark_eyes == True:
            self.__dark_eyes = False

        else:
            self.__dark_eyes = True
        self.draw_face()


def main():
    face = Face ()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")

        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else"happy"
        eyes = "blue" if face.is_dark_eyes() else"black"

        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()