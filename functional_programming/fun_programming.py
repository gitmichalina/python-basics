from functools import reduce


def biggest(values):
    big = values[0]
    for v in values:
        if v > big:
            big = v
    return big


def most(values, more):
    best = values[0]
    for v in values:
        if more(v, best):
            best = v
        return best


def larger(a, b):
    return a > b

def longer(a, b):
    return len(a) > len(b)


most([1, 6, 1, 8, 0], larger)
most(["a", "generic", "list"], longer)

#lambda a, b: len(a) > len(b)
#lambda a, b: a > b

most(["a", "generic", "list"], lambda a, b: len(a) > len(b))
most([1, 2, 3], lambda a, b: a > b)

my_list = [3, 1, 4, 1, 6]

map(lambda x: x * x, my_list)
# zwróci 9, 1, 16, 1, 36
filter(lambda x: x > 1, my_list)
# zwróci 3, 4, 6
reduce(lambda x, y: x + y, my_list)
# zwróci 15