# Jonathan Mecham
# Comp Science 1400
# program generates beautiful and exotic patterns



import pattern


def main ():
    pattern.setup ()

    playAgain = True

    while playAgain:
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        if mode == 1:
            centerX = eval(input("Enter center x position:"))
            centerY = eval(input("Enter center y position:"))
            offset = eval(input("Enter offset:"))
            width = eval(input("Enter rectangle width:"))
            height = eval(input("Enter rectangle height:"))
            count = eval(input("Enter number of rectangles:"))
            rotation = eval(input("Enter the rotation of each rectangle:"))
            pattern.drawRectanglePattern(centerX ,centerY, offset, width, height, count, rotation)


        elif mode == 2:
            centerX = eval(input("Enter center x position:"))
            centerY = eval(input("Enter center y position:"))
            offset = eval(input("Enter offset:"))
            radius = eval(input("Enter circle radius:"))
            count = eval(input("Enter number of circles:"))
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)


        elif mode == 3:
            patternNumber = eval(input("Enter number of patterns:"))

            pattern.drawSuperPattern(patternNumber)




        print()
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        if response == 1:
            playAgain = True

        elif response == 2:
            pattern.reset()
            playAgain = True

        elif response == 3:
            break

    print ("Thanks for playing dude!")
    pattern.done()
main()