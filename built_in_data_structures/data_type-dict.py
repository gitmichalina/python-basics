def main():

    # tworzenie słownika
    my_dict = {"Marta": 38, "Misia": 37, "Gaston": 5, 999: "nie wiem"}

    # Pobieranie wartości

    # sposób 1. Wyrzuca KeyError jeśli klucza nie ma
    number = my_dict["Marta"]

    # sposób 2. Zwraca None jeśli klucza nie ma
    number = my_dict.get("Marta")

    # sposób 3. Zwraca wartość domyślną jeśli klucza nie ma (tu 0)
    number = my_dict.get("Marta", 0)

    # dodawanie do słownika nowego klucza lub podmiana wartości dla istniejącego
    my_dict["Kasia"] = 39
    my_dict["Gaston"] = 999

    # usuniecie ze słownika. Wyrzuca KeyError jeśli nie ma klucza.
    # do testu czy jest takiklucz, można używac in set lub not in set
    del my_dict["Gaston"]


    # LOOPING OVER DICT

    # drukowanie klucza - tak jak w liscie i secie, ale zmienna petli jest klucz, a nie para klucz : wartość
    for k in my_dict:
        print(k)  # prints just the keys

    # to samo z metodą keys
    for k in my_dict.keys():
        print(k) # prints just the keys

    # to samo z metodą values
    for v in my_dict.values():
        print(v)  # prints just the values

    # drukowanie klucza i wartości

    for k in my_dict:
        print(k, "->", my_dict[k])

    # metoda items - zwraca tuple (key, value)
    for t in my_dict.items():
        print(t)  # prints (key, value) tuples
    # w rzeczywistosci nie jest to lista tylko dynamic view (dynamiczny widok) elementów dict.
    # każdy item jest tuple (key, value) ale jeśli zmienimy coś w trakcie loopowania będą nieprzewidziane wyniki.
    # tuples mogą być bezpośrednio unpacked do pętli for, czyli
    for k, v in my_dict.items():
        print(k, "is", v)










if __name__ == "__main__":
    main()
