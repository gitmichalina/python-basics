def main():

    # from int to float
    int_number = 3
    int_to_float = float(int_number)
    print(int_to_float, type(int_to_float))

    # from float to int
    float_number = 4.758
    float_to_int = int(float_number)
    print(float_to_int, type(float_number))

    # from real to complex
    real = 2
    imag = 5
    to_complex = (complex(real, imag))
    print(to_complex, type(to_complex))

    # from int/float to string
    price_cake = 15
    price_cookie = 6
    total = price_cake + price_cookie
    # print("The total is: " + total + "$") TypeError - can't convert 'int' object to str implicitly
    print("The total is: " + str(total) + "$")

    # from string to int/float
    price_cake = '15'
    price_cookie = '6'

    # String concatenation
    total = price_cake + price_cookie
    print("The total is: " + total + "$") # result is wrong, 156!

    # Explicit type conversion to integer
    total = int(price_cake) + int(price_cookie)
    print("The total is: " + str(total) + "$")

    # Type Conversion to Tuples and Lists

    a_tuple = ('a', 1), ('b', 2), ('c', 3)
    b_list = [1, 2, 3, 4, 5]

    tuple_to_list = list(a_tuple)
    list_to_tuple = tuple(b_list)

    print(tuple_to_list)
    print(list_to_tuple)

    # convert the chars in a string to indiv items in a tuple
    first_name = 'Misia'
    string_to_tuple = tuple(first_name)

    print(string_to_tuple)

    # Convert a string into a list
    my_list = list(first_name)
    my_list.append('linka')
    print(my_list)

    # Type Conversion to Dictionaries, and Sets
    a_tuple = ('a', 1), ('b', 2), ('c', 3)
    b_list = [1, 2, 3, 4, 5]

    tuple_to_dict = dict(a_tuple)
    list_to_set = set(b_list)

    print(tuple_to_dict)
    print(list_to_set)

    # Convert Binary to Decimal in Python

    # convert integer to binary
    int_number = 79
    binary_number = bin(int_number)
    print(binary_number)

    # convert binary tu integer
    int_number_again = int(binary_number, 2)  # Base 2(binary)
    print(int_number_again)

    # Convert Octal to Decimal in Python

    # convert integer to octal
    int_number = 79
    oct_number = oct(int_number)
    print(oct_number)

    # convert octal to integer
    int_number_again = int(oct_number, 8)
    print(int_number_again)

    # Convert Hexadecimal to Decimal in Python

    # convert integer to hexadecimal
    int_number = 79
    hexadecimal_number = hex(int_number)
    print(hexadecimal_number)

    # convert hexadecimal to integer
    int_number_again = int(hexadecimal_number, 16)
    print(int_number_again)

    # Convert Unicode Integers to Character

    # convert unicode integers to string
    d_str = chr(68)
    a_str = chr(65)
    t_str = chr(84)
    print(d_str, a_str, t_str, a_str)
    # D A T A

    # convert string to unicode integers
    chr1 = ord(d_str)
    chr2 = ord(a_str)
    chr3 = ord(t_str)
    chr4 = ord(a_str)
    print(chr1, chr2, chr3, chr4)
    # 68 65 84 65


    # round
    print(round(56.78))
    # 57

    print(round(56.78546546, 3))
    # 56.785

    print(round(56, 3))
    # 56

    #
    print(0 > True)

    #
    x = 4
    x == 5 if (True == 0) else x = 6
    print(x)


















if __name__ == "__main__":
    main()
