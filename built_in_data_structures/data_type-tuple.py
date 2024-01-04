def main():

    #można zapisywać bez nawiasów
    a, b, c = 1, 2, 3

    # pusta tuple
    # tuple = ()

    # tuple z jednym elementem ma przecinek inaczej będzie integerem
    tuple = (3, )

    # tworzenie tuple
    x = (1, 2, 3)
    x = 1, 2, 3

    # przypisanie wartości liczbom przez tuple
    a, b, c = x
    a, b, c, = "xyz"

    # pobranie wartości
    y = x[1]

    # pobranie fragmentu tuple
    z = x[1:]

    # zamiana wartości
    a, b = b, a



    # tuple jako typ wracany. wynik dzielenia i modulo tych dwóch liczb
    tuple = divmod(20, 7)



if __name__ == "__main__":
    main()
