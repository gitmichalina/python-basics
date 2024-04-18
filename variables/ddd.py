c = "misia"
d = "misia"
print(c == d)
print(c is d)

def foo():
    big_a = "w"
    big_b = "wdwd"
    big_c = "lolo"
    print(big_a == big_b)
    print(big_a is big_b)
    print("id(big_a) = %d, id(big_b) = %d" % (id(big_a), id(big_b)))


import dis

foo()
dis.disassemble(foo.__code__)
print(help("keywords"))