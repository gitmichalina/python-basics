def main():

    #można zapisywać bez nawiasów
    a, b, c = 1, 2, 3

    # creating zero-tuple
    zero_tuple = ()
    print(zero_tuple)

    # creating one-tuple
    one_tuple = (3, )
    print(one_tuple)

    # creating three-tuple
    x = (1, 2, 3)
    x = 1, 2, 3

    # assigning values
    a, b, c = 1, 2, 3
    # a is 1
    a, b, c, = "xyz"
    # a is "x"

    # getting a value
    y = x[1]

    # slicing a tuple
    z = x[1:]

    # replacing values in variables
    a, b = b, a



    # tuple as a return type
    tuple_result = divmod(20, 7)

    # illegal changing contents
    my_tuple = 1, 2, 3
    x[0] = 5



if __name__ == "__main__":
    main()
