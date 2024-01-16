x_glob = 10


def foo1():
    global x_glob
    x_glob = 20
    print(x_glob)

def foo2():
    globals()['x_glob'] = 90
    print(x_glob)

print(x_glob)
foo1()
print(x_glob)
foo2()
print(x_glob)
