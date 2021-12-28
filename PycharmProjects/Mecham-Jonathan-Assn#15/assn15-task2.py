from deck import Deck
from card import Card
import time


def getHandValue(inputList, playerNum):
    sum = 0
    for i in inputList[playerNum][2]:
        sum += Card.getCardValue(i)
    return sum


def getWinReward(inputList, playerNum):
    reward = inputList[playerNum][3] + inputList[playerNum][1]
    return reward

def getLoseReward(inputList, playerNum):
    reward = inputList[playerNum][1] - inputList[playerNum][3]
    return reward


def displayBalance(inputList, numPlayers):
    count = 0
    for i in range(numPlayers - 1):
        print(inputList[count][0], "$", inputList[count][1])
        count +=1

def main():
    run = True
    while run:
        players = []
        playerNames= ["player 1", "player 2", "player 3", "player 4", "player 5"]
        balance = 100
        dealerHand = []
        d = Deck()

        #Setup game (number of players, account balances)
        numPlayers = eval(input("how many players? (1-5):"))
        nameCount = 0
        for i in range(numPlayers):
            players.append([])
            for j in range(1):
                players[i].append(playerNames[nameCount])
                players[i].append(balance)
                players[i].append([])
                nameCount +=1

        #setup Dealer
        numPlayers +=1
        players.append(["Dealer", 100, dealerHand])

        d.shuffle()

        #Rounds(takes bets)
        betCount = 0
        #(-1 so it doesn't take dealer's bet)
        for i in range(numPlayers - 1):
            for i in range(1):
                print(players[betCount][0], "'s turn")
                bet = 0
                while bet < 5:

                    bet = eval(input("how much would you like to bet?(Must be atleast 5$):"))


                    players[betCount].append(bet)
                betCount += 1
                #print(players[betCount])

        #Rounds(deals 2 cards to each player one card at a time)
        for i in range(2):
            dealCount = 0
            for i in range(numPlayers):
                players[dealCount][2].append(d.draw())
                dealCount += 1

        #Display Dealer's 2nd card
        print("The dealer's 2nd card is:", players[-1][2][-1])

        turnCount = 0
        while turnCount < numPlayers -1:
            print(players[turnCount][0],"'s turn")
            print("your hand", players[turnCount][2])
            move = eval(input("1)Hit or 2)Hold:"))

            #hit
            if move == 1:
                players[turnCount][2].append(d.draw())
                if getHandValue(players, turnCount) > 21:
                    print("Your hand", players[turnCount][2])
                    print("YOU BUST!")
                    turnCount += 1

            #hold
            elif move == 2:
                turnCount += 1

        #Dealer's turn
        print('''
        The dealers cards are:''')
        for i in players[-1][2]:
            time.sleep(1)
            print (i)
        while getHandValue(players, -1) < 17:
            print("the Dealer takes a card")
            time.sleep(1)
            players[-1][2].append(d.draw())
        if getHandValue(players, -1) > 21:
            print("The Dealer BUSTS!")
        else:
            print("The Dealer holds")



        #determine winner
        winCount = 0
        while winCount < numPlayers - 1:
            #Dealer busts and player doesnt
            if getHandValue(players, winCount) < 21 and getHandValue(players, -1) > 21:
                print(players[winCount][0], "wins!")

                #award winning money
                players[winCount][1] = getWinReward(players, winCount)

            #Dealer and Player tie
            if getHandValue(players, winCount) == getHandValue(players, -1):
                print(players[winCount][0], "and Dealer Tie!")


            #Dealer and player are both lower than 21 but dealer is higher(player loses)
            if getHandValue(players, winCount) < getHandValue(players, -1) and getHandValue(players, -1) < 21:
                print(players[winCount][0], "loses!")

                players[winCount][1] = getLoseReward(players, winCount)

            #opposit ^ (player wins)
            if getHandValue(players, -1) < getHandValue(players, winCount) and getHandValue(players, winCount) < 21:
                print(players[winCount][0], "wins!")

                players[winCount][1] = getWinReward(players, winCount)

            #if everyone busts
            if getHandValue(players, winCount) > 21 and getHandValue(players, -1) > 21:
                print(players[winCount][0], "loses!")

                players[winCount][1] = getLoseReward(players, winCount)

            #player busts but Dealer doesnt
            if getHandValue(players, winCount) > 21 and getHandValue(players, -1) < 21:
                print(players[winCount][0], "loses!")

                players[winCount][1] = getLoseReward(players, winCount)

            winCount +=1


        #display user Balances
        displayBalance(players, numPlayers)

        print("Would you like to play again?")
        menu = eval(input("1)yes or 2)no"))
        if menu == 1:
            run = True
        if menu == 2:
            print("thanks for playing")
            run = False







main()
