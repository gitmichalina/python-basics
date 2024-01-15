global counter
counter = 0


def main():
    global counter
    counter += 1
    print(counter)
    func_1()
    print(counter)


def func_1():
    global counter
    counter += 1
    enc_var = 4
    print(enc_var)

    def func_2():
        nonlocal enc_var
        enc_var += 2

    func_2()
    print(enc_var)


def func_3():
    pass


if __name__ == '__main__':
    main()
