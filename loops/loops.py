import random

import requests


def main():
    """
    This is myyyy main function
    """
    for i in [5, 4, 3, 2, 1]:
        print(i, end=' ')
    print("Blast off!")

    for i in range(5, 0, -1):
        print(i, end=' ')
    print("Blast off!")

    help(main)
    help(requests.Request)


def while_loop():
    n = 5
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")

    # works the same as:

    n = 6
    while (n := n - 1) > 0:
        print(n, end=' ')
    print("Blast off!")


def off():
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    faces = ["Jack", "Queen", "King", "Ace"]
    numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    deck = set()

    for suit in suits:
        for card in faces + numbered:
            deck.add((card, "of", suit))

    print(type(deck))
    print(len(deck))

    card = random.choice(list(deck))
    print(card)
    print(type(card))
    deck.remove(card)
    print(len(deck))

    n = 5
    while n > 0:
        print(n)
    n -= 1
    print("Blast off!")


if __name__ == "__main__":
    main()