def cool():
    pass


def cookie():
    ...


def main():
    # one-line if statements

    if "aul" in "grault":  # Truthy
        print("yes")
        print("another")

    if "quux" in ["foo", "bar", "baz"]:  # Falsy
        print("yes")

    # else and elif clauses
    x = 20
    if x < 50:
        print("(first suite)")
        print("x is small")
    else:
        print("(second suite)")
        print("x is large")

    # elif
    name = "john"
    if name == "Marta":
        print("Hi Marta")
    elif name == "Misia":
        print("Hi Misia")
    elif name == "Gaston":
        print("Hi Gaston")
    else:
        print("I don't know")

    var = 3
    if "M" in "Misia":
        print("Hi Marta")
    elif 1 / 0:
        print("This won't happen")
    elif var:
        print("This won't either")

    # multiple statement
    x = 2

    if x == 1:
        print("foo")
        print("bar")
        print("baz")
    elif x == 2:
        print("qux")
        print("quux")
    else:
        print("corge")
        print("grault")

    # ternary operator
    age = 23
    s = ("minor" if age < 21 else "adult")
    print(s)

    raining = False
    print("Let's go to the", "beach" if not raining else "library")

    print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')

    # selecting variable to assign
    a = 10
    b = 5

    if a > b:
        m = a
    else:
        m = b

    # ternary and precedence

    x = y = 40

    z = 1 + x if x > y else y + 2
    # z = 42

    z = (1 + x) if x > y else (y + 2)
    # z = 42

    z = 1 + (x if x > y else y) + 2
    # z = 43

    # chained conditional expressions
    s = ('foo' if (x == 1) else
         'bar' if (x == 2) else
         'baz' if (x == 3) else
         'qux' if (x == 4) else
         'quux')
    # s = 'baz'


if __name__ == "__main__":
    main()
