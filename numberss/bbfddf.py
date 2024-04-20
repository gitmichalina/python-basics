number = 43

validation_conditions = (
    isinstance(number, int),
    number % 2 == 0,
)

print(all(validation_conditions))

number = 43
print(callable(number))
print(callable(print))