def main():

    # tworzenie pustej listy

    empty_list = []

    # tworzenie pełnej listy

    my_list = [1, 2, 3]

    # tworzenie listy o konkretnej wielkości (mnożenie jej przez integera)

    new_list = [3, 2] * 2
    # [3, 2, 3, 2]

    # tworzenie listy przez factory metod
    faxtory_list = list()
    # []

    # dostęp do elementu, zmiana wartości

    my_list[0] = 8   # pierwszy element
    my_list[-1] = 9  # ostatni element

    # zwraca liczbę elementów
    len(my_list)

    # zwraca kopię listy order asc (kolejność rosnąca)
    sorted(my_list)

    element = 3
    # dodaje element na koniec listy i zwraca None
    my_list.append(element)

    # usuwa ostatni element z listy i go zwraca
    my_list.pop()

    # sortuje liste i zwraca None
    my_list.sort()

    # tworzenie nowej listy z fragmentu innej listy (slice), podajemy indeksy
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







if __name__ == "__main__":
    main()
