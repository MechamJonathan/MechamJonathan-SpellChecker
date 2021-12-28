# Jonathan Mecham
# A01854679
# comp science 1400
# Assn#7 task 1 v.1
# Program plays rock, paper, scissors! taking the user's input and challenging it against the computer's.



import random

hand = int(input("Enter hand: scissor (0), rock (1), paper (2):"))

comp_hand = random.randint (0,2)


def move(x):
    if x == 0:
        return "Scissor"
    if x == 1:
        return "Rock"
    if x == 2:
        return "Paper"

if comp_hand == hand:
    print ("The computer is " + move(comp_hand) + ", You are " + move(hand) +" too. It's a draw!")
elif comp_hand == hand + 1:
    print ("The computer is " + move(comp_hand) + ", You are " + move(hand) + ". Computer wins!")
elif comp_hand == hand - 2:
    print ("The computer is " + move(comp_hand) + ", You are " + move(hand) + ". Computer wins!")
elif comp_hand == hand -1:
    print ("The computer is " + move(comp_hand) + ", You are " + move(hand) + ". You win!")
elif comp_hand == hand +2:
    print ("The computer is " + move(comp_hand) + ", You are " + move(hand) + ". You win!")