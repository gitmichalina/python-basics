def main():

    # creating an empty dict
    empty_dict = {}

    # creating a non-empty dict
    my_dict = {"Marta": 38, "Misia": 37, "Gaston": 5, 999: "nie wiem"}

    # Getting a value

    my_dict = {"Marta": 38, "Misia": 37, "Gaston": 5, 999: "nie wiem"}

    # 1. If the key is not found, a KeyError will result.
    number = my_dict["Marta"]

    # 2. If the key is not found, the value None is returned.
    number = my_dict.get("Marta")

    # 3. returns the value associated with key, or the default_value if there is no such key.  (here is 0)
    number = my_dict.get("Marta", 0)


    # adding something to the dictionary or changing the value associated with the key
    my_dict["Kasia"] = 39
    my_dict["Gaston"] = 999

    # usuniecie ze słownika. Wyrzuca KeyError jeśli nie ma klucza.
    # do testu czy jest takiklucz, można używac in set lub not in set
    del my_dict["Gaston"]

    # conversion from a dict

    # When we convert from a dict to any of the other types, you get only the keys, not the values.

    my_dict = {"Marta": 38, "Misia": 37, "Gaston": 4}
    print(set(my_dict))
    # {'Gaston', 'Marta', 'Misia'}
    print(list(my_dict))
    # ['Marta', 'Misia', 'Gaston']
    print(tuple(my_dict))
    # ('Marta', 'Misia', 'Gaston')

    # conversion from a dict
    # We can convert a list, set, or tuple to a dict only if the elements are grouped in twos, for example, a list of 2-tuples (tuples with two elements).

    my_list = [("Marta", 38), ("Misia", 37), ("Gaston", 5)]
    my_dict = dict(my_list)
    #{'Marta': 38, 'Misia': 37, 'Gaston': 5}



    # LOOPING OVER DICT

    # loop variable is the key
    for k in my_dict:
        print(k)  # prints just the keys

    #
    for k in my_dict.keys():
        print(k) # prints just the keys

    #
    for v in my_dict.keys():
        print(v)  # prints just the values

    # drukowanie klucza i wartości

    for k in my_dict:
        print(k, "->", my_dict[k]) # prints keys and values


    # items() returns tuple (key, value)
    for t in my_dict.items():
        print(t)  # prints (key, value) tuples
    # w rzeczywistosci nie jest to lista tylko dynamic view (dynamiczny widok) elementów dict.
    # każdy item jest tuple (key, value) ale jeśli zmienimy coś w trakcie loopowania będą nieprzewidziane wyniki.
    # tuples mogą być bezpośrednio unpacked do pętli for, czyli
    for k, v in my_dict.items():
        # v = "koko"
        print(k, "is", v)
        print(my_dict.items())
        # koko is 38
        # dict_items([('Marta', 38), ('Misia', 37), (999, 'nie wiem'), ('Kasia', 39)])
        # koko is 37
        # dict_items([('Marta', 38), ('Misia', 37), (999, 'nie wiem'), ('Kasia', 39)])
        # koko is nie
        # wiem
        # dict_items([('Marta', 38), ('Misia', 37), (999, 'nie wiem'), ('Kasia', 39)])
        # koko is 39
        # dict_items([('Marta', 38), ('Misia', 37), (999, 'nie wiem'), ('Kasia', 39)])











if __name__ == "__main__":
    main()
