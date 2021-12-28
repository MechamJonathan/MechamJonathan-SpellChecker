
class Polygon:
    def __init__(self):
        self.__sides1 = eval(input("how many sides on polygon 1?:"))
        self.__sides2 = eval(input("howmanysides on polygon 2?:"))

    def __add__(self):
        print("polygon 1 + polygon 2:", self.__sides1 + self.__sides2)

    def __sub__(self):
        print("polygon 1 - polygon 2:", self.__sides1 - self.__sides2)

    def __lt__(self):
        if self.__sides1 < self.__sides2:
            print ("polygon 1 < polygon 2:", True)

        else:
            print ("polygon 1 < polygon 2:", False)

    def __gt__(self):
        if self.__sides1 > self.__sides2:
            print ("polygon 1 > polygon 2:", True)

        else:
            print ("polygon 1 > polygon 2:", False)

    def __eq__(self):
        if self.__sides1 == self.__sides2:
            print ("polygon 1 = polygon 2:", True)

        else:
            print ("polygon 1 = polygon 2:", False)

    def __len__(self):
        print("length of polygon 1:",self.__sides1, ", Length of polygon 2:" , self.__sides2)

    def __str__(self):
        print ("polygon 1 and polygon 2 are strings:", True)