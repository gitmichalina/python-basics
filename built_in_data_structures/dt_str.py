from math import pi


def main():

    y = 'Hello'
    # nie mozna przypisac, bo 'str' object does not support item assignment
    # y[0] = 'm'
    print(y)
    z = 'HelloWorld'[0]
    print(z)
    my_string = "Misia"
    my_string2 = "Koko"

    # Przydatne metody
    my_string.split(my_string2)
    my_string.join('a')

    # sformatowany string czyli f-string
    print(f"pi is {{round(pi, 4)}}.")



if __name__ == "__main__":
    main()
