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
# draws
if comp_hand == 0 and hand == 0 or comp_hand == 1 and hand == 1 or comp_hand == 2 and hand == 2:
    print("The computer is " + move(comp_hand) + ", You are " + move(hand) + " too. It's a draw!")

# computer wins
if comp_hand == 1 and hand == 0 or comp_hand == 2 and hand == 1 or comp_hand == 0 and hand == 2:
    print("The computer is " + move(comp_hand) + ", You are " + move(hand) + ". Computer wins!")

# user wins
if comp_hand == 0 and hand == 1 or comp_hand == 1 and hand == 2 or comp_hand == 2 and hand == 0:
    print("The computer is " + move(comp_hand) + ", You are " + move(hand) + ". You win!")