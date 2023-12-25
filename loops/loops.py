import random


def main():
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


if __name__ == "__main__":
    main()