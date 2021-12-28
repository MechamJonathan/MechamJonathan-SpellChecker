# Jonathan Mecham
# Comp Science 1400
# Assn14 Task 3
# program creates card game as outlined in the assignment description




from deck import Deck
import sys



def selectionSort(inputList):
    for i in range(len(inputList) - 1):
        currMinIndex = i

        for j in range(i + 1, len(inputList)):
            if inputList[currMinIndex] > inputList[j]:
                currMinIndex = j

        if currMinIndex != i:
            inputList[i], inputList[currMinIndex] = inputList[currMinIndex], inputList[i]


mano = ["Rock", "Paper", "Scissors"]
coin = ["Heads", "Tails"]
maxCardValue = 20

# Make sure you understand this to do the opposite conversion!!!
def convertCardToValue(cardValue, cardMano, cardCoin):
    return 2 * ((cardValue - 1) + (maxCardValue * mano.index(cardMano))) + coin.index(cardCoin)





def binary_search(input_list, key):
    print(input_list)
    low = 0
    high = len(input_list) - 1
    while high >= low:
        print(low, high)
        mid = (high + low) // 2
        if key == input_list[mid]:
            return mid
        elif key < input_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1





def main():
    deck = Deck()

    playerHand = []

    for i in range(30):
        playerHand.append(deck.draw())

    for j in playerHand:
        print(j)



    print('''
    1) sort by value 
    2) sort by id
    3) find card
    4) new hand
    5) quit 
    ''')
    menu = eval(input("make a selection:"))

    if menu == 1:
        selectionSort(playerHand)
        for card in playerHand:
            print(card)


    if menu == 2:
        return

    if menu == 3:
        valueKey = eval(input("enter card value to search for:"))
        coinKey = eval(input('''enter coin to search for:
        1) heads
        2) tails'''))
        manoKey = eval(input('''enter mano to search for:
        1) Rock
        2) Paper
        3) Scissors'''))

        valueResult = binary_search(playerHand, valueKey)
        coinResult = binary_search(playerHand, coinKey)
        manoResult = binary_search(playerHand, manoKey)


        if valueResult and coinResult and manoResult == -1:
            print("Did not find card")
        else:
            print("The card is in your hand!")



    if menu == 4:
        for i in playerHand:
            playerHand.pop()

        for i in range(30):
                playerHand.append(deck.draw())

        for j in playerHand:
                print(j)


    if menu == 5:
        print("thanks for playing!")
        sys.exit()
















main()