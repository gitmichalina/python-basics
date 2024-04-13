class Dog:
    pass


a = Dog()
b = Dog()

print(a)
print(b)

print(a == b)

a = "kkk"
b = "kkk"
c = str("kkk")

print(id(a))
print(id(b))
print(id(c))