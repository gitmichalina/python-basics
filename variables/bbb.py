# small_a = 255
# small_b = 255
# print(id(small_a))
# print(id(small_b))
# print(small_a == small_b)
#
# big_a = 46004600
# big_b = 46004600
# print(id(big_a))
# print(id(big_b))
# print(big_a == big_b)


def foo():
    big_a = 300
    big_b = 300
    print(big_a == big_b)
    print(big_a is big_b)
    print("id(big_a) = %d, id(big_b) = %d" % (id(big_a), id(big_b)))


import dis

foo()
dis.disassemble(foo.__code__)
