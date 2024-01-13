def main():

    # creating an empty list using constructor []
    empty_list = []

    # creating an empty list using list()
    empty_list_2 = list()

    # creating a non-empty list
    my_list = [1, 2, 3]
    my_hetero_list = [1, 2, 'a', 'b']
    my_none_list = [None] * 5
    print(my_none_list)

    # creating a list with fixed number of values
    new_list = [3, 2] * 2
    # [3, 2, 3, 2]

    # getting an element
    my_list[0] = 8   # first element
    my_list[-1] = 9  # last element

    # modifying an element
    my_hetero_list = [1, 2, 'a', 'b']
    my_hetero_list[0] = "zamiast 0 bedzie ten string"




    # return a number of elements
    number_of_elements = len(my_list)

    # returns a copy of a list with ascending order
    ordered_list = sorted(my_list)

    element = 3
    # adds an element to the ned of the list and returns None
    my_list.append(element)

    # removes the last element and returns it
    my_list.pop()

    # sorts list and returns None
    my_list.sort()

    # creating a new list from another sliced list.
    index_X = 1
    index_Y = 2

    # lista od indeksu X do indeksu Y (bez indeksu Y)
    sliced_list = my_list[ index_X : index_Y ]

    # lista od indeksu X do końca)
    sliced_list = my_list[ index_X : ]

    # lista od początku (indeks zerowy) do indeksu_Y
    sliced_list = my_list[:index_Y]

    # kopia całej listy
    sliced_list = my_list[:]

    # można używać liczb ujemnych. Ostatni element to -1
    # lista od początku do końca ale bez ostatniego elementu
    sliced_list = my_list[:-1]

    # nowa lista co drugi element (licząc od zerowego indeksu
    sliced_list = my_list[::2]

    # podmiana fragmentu listy, przypisanie nowych wartości
    my_list = [0, 1, 2, 3]
    my_list[4:] = [6]
    # [0, 1, 2, 3, 6]

    # można użyć stringa jaki listy
    x = "abcdef"[2:5]
    # cde

    # można mieć listę list
    grades = [["Marta", 5], ["Misia", 4]]
    grades[1][0] = "Misia_M"

    # tworzenie listy list źle
    wrong_creation = [[None] * 3] * 2

    # tworzenie listy list dobrze.
    # Najpierw lista zer, a potem pelą zastępuję każde 0 listą zer.

    x = [0] * 3
    for i in range(0, 3):
        x[i] = [0] * 3
    # x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # LOOPING OVER LIST

    # chcemy coś zrobić z każdym elementem
    for e in my_list:
        print(e)

    # chcemy coś zrobić z tym elementem i jego pozycją na liście
    for i in range(0, len(my_list)):
        print(my_list[i], "is at", i)

     # lub (zwykle nie używa się loop do pobierania indeksów

    for index, value in enumerate(my_list):
        print(value, "is at", index)










if __name__ == "__main__":
    main()
