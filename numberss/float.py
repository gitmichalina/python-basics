from numpy import array
import textwrap
y=array([0, 1])

try:
    bool(y)
except ValueError as exc:
    print("\n".join(textwrap.wrap(str(exc))))

print(bool([]))

print(len([]))

a = "this"
b = "this"

print(a==b)
print(a is b)

print(id(a))
print(id(b))
