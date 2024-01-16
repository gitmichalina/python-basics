
def enclosing_f():
    x = 20
    print(x)

    def enclosed_f():
        nonlocal x
        x = 10
        print(x)

        return

    enclosed_f()
    print(x)
    return



enclosing_f()