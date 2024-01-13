word = 'generator'
gen = (c for c in word if c in 'aeiou')
print(type(gen))
for i in gen:
    (print(i, end=' '))


def powers_of_two():
    n = 2
    for i in range(0, 5):
        yield n
        n *= 2

def foo(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

gen = powers_of_two()
print(type(gen))
for n in gen:
    print(n, end=' ')

gen = powers_of_two()
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

def foo(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)