def main():
    deck = set()
    print(type(deck))
    print(len(deck))
    print(dir(deck))
    deck.add("ss")


def searching_in_set():
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    faces = ["Jack", "Queen", "King", "Ace"]
    numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    deck = set()

    for suit in suits:
        for card in faces + numbered:
            deck.add((card, "of", suit))

    card = ("Ace", "of", "Hearts")

    if card in deck:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
