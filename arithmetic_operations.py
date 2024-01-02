def main():
    # x = 10 // -2
    # y = 10.0 // -2
    # z = 10.0 // -2.0
    #
    # a = 10 / 2
    # b = 10.0 / 2
    # c = 10.0 / 2.0
    #
    # print(x, y, z, a, b, c, sep="\n")

    x = 10 % -3
    y = 10.0 % -3
    z = 10.0 % -3.0

    print(x, y, z, sep="\n")

    x = -10 % 3
    y = -10.0 % 3
    z = -10.0 % 3.0

    print(x, y, z, sep="\n")

    x = 10 % 3
    y = 10.0 % 3
    z = 10.0 % 3.0

    print(x, y, z, sep="\n")

    x = -10 % -3
    y = -10.0 % -3
    z = -10.0 % -3.0

    print(x, y, z, sep="\n")


if __name__ == "__main__":
    main()