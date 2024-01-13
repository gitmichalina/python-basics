from functools import reduce


def biggest(values):
    the_biggest_value = values[0]
    for value in values:
        if value > the_biggest_value:
            the_biggest_value = value
    return the_biggest_value


def the_most_value(values, comparing_function):
    current_best_value = values[0]
    for value in values:
        if comparing_function(value, current_best_value):
            current_best_value = value
    return current_best_value


def larger(a, b):
    return a > b

def longer(a, b):
    return len(a) > len(b)


the_most_value([1, 6, 1, 8, 0], larger)
the_most_value(["a", "generic", "list"], longer)

#lambda a, b: len(a) > len(b)
#lambda a, b: a > b

the_most_value(["a", "generic", "list"], lambda a, b: len(a) > len(b))
the_most_value([1, 2, 3], lambda a, b: a > b)

my_list = [3, 1, 4, 1, 6]

map(lambda x: x * x, my_list)
# zwróci 9, 1, 16, 1, 36

print(list(map(lambda x: x * x, my_list)))

filter(lambda x: x > 1, my_list)

print(list(filter(lambda x: x > 1, my_list)))
# zwróci 3, 4, 6


reduce(lambda x, y: x + y, my_list)

print(reduce(lambda x, y: x + y, my_list))
# zwróci 15