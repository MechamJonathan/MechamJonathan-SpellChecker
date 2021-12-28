

class Card:
    def __init__(self, value):
        self.__value = value
        self.__Ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        self.__coin = ["heads", "tails"]
        self.__mano = ["rock", "paper", "scissors"]


    def getRank(self):
        return self.__Ranks[self.__value % 20]

    def getCoin(self):
        return self.__coin[self.__value // 20]

    def getMano(self):
        return self.__mano[self.__value // 20]

    def getCardValue(self):
        return self.__value % 20 + 1

    def getDeckValue(self):
        return self.__value

    def __str__(self):
        return self.getRank() +  " of " + self.getMano() + " " + self.getCoin()

    def __repr__(self):
        return self.__str__()
