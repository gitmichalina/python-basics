def main():

    # tworzenie pustego setu źle
    wrong_creation_it_is_a_dict = {}

    # tworzenie pustego setu dobrze
    empty_set = set()

    # loopowanie przez set
    s = {10, "ten", "X"}

    for elem in s:
        print(elem)

    # konwersja do listy
    list_of_s = list(s)

    # konwersja do setu
    lista = list()
    nowy_set = set(lista)

    # operacje union, intersection, difference  set difference

    set1 = {0, 1, 2, 3}
    set2 = {2, 3}

    # zwraca set elementów, które są w set1 lub  set2, albo w obu setach (UNION)
    union_set = set1 | set2
    union_set = set1.union(set2)

    # zwraca set elementów, które są zarówno w set1 jak i set2 (INTERSECTION)
    intersection_set = set1 & set2
    intersection_set = set1.intersection(set2)

    # zwraca set z elementami, które są w set1 ale nie w set2 (DIFFERENCE)
    difference_set = set1 - set2
    difference_set = set1.difference(set2)

    # zwraca set z elementami, które są tylko w jednym z tych setów (SYMMETRIC DIFFERENCE)
    symmetric_difference_set = set1 ^ set2
    symmetric_difference_set = set1.symmetric_difference(set2)

    # zwraca True jesli każdy element z set1 jest w set2 (IS SUBSET)
    issubset_set = set1.issubset(set2)

    # zwraca True jesli każdy element z set2 jest też w set1 (IS SUPERSET)
    issuperset_set = set1.issuperset(set2)

    # użycie znaków porównania dla subset/superset i równe/nierówne w relacji między setami.

    # set1 jest proper subset setu2 (set1 jest subsetem set2, ale jest mu równy
    set1 < set2 == True

    my_set = {1, 3}
    element = 2
    # dodawanie elementów. Jeśli element jest już w secie, nic się nie dzieje. I tak zwraca None
    my_set.add(element)

    # usunięcie elementu jeśli jest obecny. Jeśli go nie ma, nic się nie dzieje
    my_set.discard(element)

    # usuniecie elementu lub wyrzucenie wyjątku KeyError jeśli go nie ma
    my_set.remove(element)

    # usunięcie i zwrócenie dowolnego elementu z setu lub wyrzucenie wyjątku jeśli jest pusty
    my_set.pop()

    # usuniecie wszystkich elementów z setu
    my_set.clear()

    # LOOPING OVER SET

    # chcemy coś zrobić z każdym elementem setu
    for e in my_set:
        print(e)

    # można też użyć enumerate, ale sety nie mogą być indeksowane







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
