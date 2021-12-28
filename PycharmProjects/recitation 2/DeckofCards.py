import random


def main():
    deck = list(range(52))
    suits = ["spades", "clubs", "hearts", "diamonds"]
    ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

    random.shuffle(deck)
    card = deck.pop()
    print(card)
    print(ranks[card % 13] + "of" + suits[card // 13])