def main():
    round(123.45678, 3)
    # zwraca zaokrąglenie do 3 cyfr czyli 123.457
    round(56.78)
    # zwraca 56, bo część po przecinku jest ucięta
    int("56")
    # zwraca integer 56
    int(5.7)
    # zwraca 5
    float(5)
    # zwraca 5.0
    float("5.7")
    # zwraca 5.7
    str(8)
    # zwraca argument w stringu
    str([1, 2, 3])
    # zwraca '[1, 2, 3]'

    bool("False")
    # zwraca True! bo "False" to niepusty string.
    # jako False uznawane są: False, None, 0, 0.0, empty strings, empty lists, empty sets, empty
    # tuples, and empty dictionaries.

    # inne typy danych, które mogą być użyte jako funkcje konwersji to:
    # list, set, tuple i dict

    # funkcja type(x)
    if (type(5) == float) is True:
        print("True")
    if (type(5) == "int") is False:
        print("False")

    print(type(5))
    print(type("lo"))
    print(type("5"))

    # funkcja isinstance(value, type). czy value jest określonego typu (value, type)?
    print(isinstance(3, int))
    print(isinstance(3, (int, float, set))) # czy jest jednym z tych typów
    print(isinstance(3, (int | float)))  # union tych dwóch typów
    # ta funkcja nie dotyczy typów generycznych! np. list[int]




if __name__ == "__main__":
    main()

