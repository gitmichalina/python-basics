# digits = [0, 1, 2, 3, 4, 5]
# print(id(digits))
#
# # creates a new list
# digits = digits + [6, 7, 8, 9]
# print(id(digits))
#
# # mutate a list
# digits += [10, 11, 12, 13, 14, 15]
# print(id(digits))
#
#
# numbers = [1, 2, 3]
# print(id(numbers))
#
# # creates a new list
# numbers = numbers * 3
# print(id(numbers))
#
# # mutate a list
# numbers *= 3
# print(id(numbers))
#


b = (2, 3)
print(id(b))
b = b + (1,2)
print(id(b))

b += (1,2)
print(id(b))
