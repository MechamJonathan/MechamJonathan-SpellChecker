

from deck import Deck
from card import Card





def bubbleSort(inputList):
    didSwap = True
    step = 1
    while didSwap:
        didSwap = False

        for i in range(len(inputList) - 1):
            if inputList[i].getCardValue() > inputList[i + 1].getCardValue():
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                didSwap = True

                stepList = [Card.getNickName(i) for i in inputList]
                print(str(step) + ":", stepList)
                step += 1




def insertionSort(inputList):
    step = 1
    for i in range(1, len(inputList)):
        currElement = inputList[i]
        j = i - 1
        stepList = [Card.getNickName(i) for i in inputList]
        print(str(step) + ":", stepList)


        while j >= 0 and inputList[j].getCardValue() > currElement.getCardValue():
            inputList[j + 1] = inputList[j]
            j -= 1

        inputList[j + 1] = currElement
        step += 1





def main():
    d = Deck()
    playerHand= []

    for i in range(20):
        playerHand.append(d.draw())
    for i in playerHand:
        print(i)

    menu = input("Would you like to 1) Bubble sort or 2) Insertion Sort?")

    if menu == "1":
        bubbleSort(playerHand)


    elif menu == "2":
        insertionSort(playerHand)

main()