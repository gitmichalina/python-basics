import math


def main():
    x = 10 // 4
    y = 10.0 // 4
    z = 10.0 // 4.0

    # 2
    # 2.0
    # 2.0

    print(x, y, z, sep="\n")
    print()

    x = 10 // -4
    y = 10.0 // -4
    z = 10.0 // -4.0

    # -3
    # -3.0
    # -3.0

    print(x, y, z, sep="\n")
    print()

    a = 10 / 4
    b = 10.0 / 4
    c = 10.0 / 4.0

    # 2.5
    # 2.5
    # 2.5

    print(a, b, c, sep="\n")
    print()

    a = 10 / -4
    b = 10.0 / -4
    c = 10.0 / -4.0

    # -2.5
    # -2.5
    # -2.5

    print(a, b, c, sep="\n")
    print()

    x = 10 % -7
    y = 10.0 % -7
    z = 10.0 % -7.0
    #
    print(x, y, z, sep="\n")
    print()
    #
    x = -10 % 4
    y = -10.0 % 4
    z = -10.0 % 4.0
    #
    print(x, y, z, sep="\n")
    print()
    #
    x = 10 % 4
    y = 10.0 % 4
    z = 10.0 % 4.0
    #
    print(x, y, z, sep="\n")
    print()
    #
    x = -10 % -4
    y = -10.0 % -4
    z = -10.0 % -4.0
    #
    print(x, y, z, sep="\n")
    print()

    """modulo with negative numbers works like this:
        mod = n - math.floor(n/base) * base
        
        for example:
        -5%4 = (-2*4 + 3) % 4 = 3
        
    """

    # f = math.fmod(-5, 4)
    # print(f)

    print(-10 % 4)
    #2
    print(-10 % 3)
    #2
    print(-10 % 7)
    #4
    print(13 % -7)
    #-1
    print(-3 % 7)
    print(math.fmod(-3, 7))


if __name__ == "__main__":
    main()