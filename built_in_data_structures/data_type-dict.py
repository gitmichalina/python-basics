def main():

    # tworzenie słownika
    age = {"Marta": 38, "Misia": 37, "Gaston": 5, 999: "nie wiem"}

    # Pobieranie wartości

    # sposób 1. Wyrzuca KeyError jeśli klucza nie ma
    number = age["Marta"]

    # sposób 2. Zwraca None jeśli klucza nie ma
    number = age.get("Marta")

    # sposób 3. Zwraca wartość domyślną jeśli klucza nie ma (tu 0)
    number = age.get("Marta", 0)

    # dodawanie do słownika nowego klucza lub podmiana wartości dla istniejącego
    age["Kasia"] = 39
    age["Gaston"] = 999

    # usuniecie ze słownika. Wyrzuca KeyError jeśli nie ma klucza.
    # do testu czy jest takiklucz, można używac in set lub not in set
    del age["Gaston"]






if __name__ == "__main__":
    main()
