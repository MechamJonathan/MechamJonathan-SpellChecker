
import random

class Deck:
    def __init__(self):
        self.__deck = list(range(52))
        self.__suits = ["spades", "clubs", "hearts", "diamonds"]
        self.__ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

    def shuffle(self):
        random.shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()

    def cardString(self, value):
        return self.__ranks[value % 13] + "of" + self.__suits[value // 13]


class Card:
    def __init__(self, value):
        self.__value = value
        self.__suits =["spades", "clubs", "hearts", "diamonds"]
        self.__ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

    def getRanks(self):
        return self.__ranks[self.__value % 13]

    def getSuit(self):
        return self.__suits[self.__value // 13]




def main():
    deck = Deck()
    deck.shuffle()

    playerHand = []
    dealerHand = []

    for i in range (2):
        playerHand.append(deck.draw())
        dealerHand.append(deck.draw())


main()