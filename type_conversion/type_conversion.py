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
        print("(type(5) == float) is True")
    if (type(5) == "int") is False:
        print("(type(5) == \"int\") is False")

    print(type(5))
    print(type("lo"))
    print(type("5"))

    # funkcja isinstance(value, type). czy value jest określonego typu (value, type)?
    print(isinstance(3, int))
    print(isinstance(3, (int, float, set))) # czy jest jednym z tych typów
    print(isinstance(3, (int | float)))  # union tych dwóch typów
    # ta funkcja nie dotyczy typów generycznych! np. list[int]

    a_int = 1
    b_float = 1.0
    c_sum = a_int + b_float
    print(c_sum)
    print(type(c_sum))

    # 2.0
    # <class 'float'>

    my_dict = {"name": "John", "age": 5, "city": "New York"}

    my_dict = {"Marta": 38, "Misia": 37, "Gaston": 4}
    print(set(my_dict))
    # {'Gaston', 'Marta', 'Misia'}
    print(list(my_dict))
    # ['Marta', 'Misia', 'Gaston']
    print(tuple(my_dict))
    # ('Marta', 'Misia', 'Gaston')









if __name__ == "__main__":
    main()

