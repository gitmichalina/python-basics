class User:
    pass


# Add instance attributes dynamically
my_user = User()
my_user.name = "Misia"
my_user.age = 23


# Add methods dynamically
def __init__(self, name, age):
    self.name = name
    self.age = age


User.__init__ = __init__

print(vars(my_user))
# {'name': 'Misia', 'age': 23}
print(User.__dict__)
# {'__module__': '__main__',
# '__dict__': <attribute '__dict__' of 'User' objects>,
# '__weakref__': <attribute '__weakref__' of 'User' objects>,
# '__doc__': None,
# '__init__': <function __init__ at 0x000002525B31A2A0>}

another_user = User("kkoko", 67)
print(vars(another_user))
# {'name': 'kkoko', 'age': 67}
