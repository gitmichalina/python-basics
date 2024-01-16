my_list = [1, 2, 3, 4]
print(sum(my_list))


def foo(name="imię", surname="nazwisko"):
    print("name:", name, "surname:", surname)


foo()
foo(name="marta", surname="dora")
foo(surname="dora", name="marta")


# name: imię surname: nazwisko
# name: marta surname: dora
# name: marta surname: dora

def add(a, b, c):
    print("add =", (a + b + c))


add(10, c=10, b=30)


# add = 50


def find_the_smallest(*args):
    global kuku
    kuku = 60
    n = args[0]
    for i in args:
        if i < n:
            n = i
    return n

kuku = 70
print(kuku)
print(find_the_smallest(4, 1, 2, 3, 4))

s = [1, 2, 3, 4, 5, 6, 7]
m = list(map(lambda i: i + 2, s))
print(m)

s = [1, 2, 3, 4, 5, 6, 7]
m = list(filter(lambda i: i % 2 == 0, s))
print(m)
