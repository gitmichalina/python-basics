class Animal():

    object_counter = 0
    @classmethod
    def increase_counter(cls):
        cls.object_counter += 1
        return cls.object_counter

    def __init__(self, name, age):
        self.name = name
        self.age = age



    def say_hi(self):
        print("hi " + self.name)


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("bark bark I am " + self.name)


gaston = Dog("gaston", 4, "British Gaston")




animal_object = Animal("weirdo", 1)
print(animal_object)


# print(dir())
# ['Animal', 'Dog', '__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'animal_object', 'gaston']

# print(vars())
# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001B3903DBE30>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\micha\\Projects\\PyCharm\\python-basics\\type_conversion\\practice_1304.py',
# '__cached__': None, 'Animal': <class '__main__.Animal'>, 'Dog': <class '__main__.Dog'>,
# 'animal_object': <__main__.Animal object at 0x000001B390755250>,
# 'gaston': <__main__.Dog object at 0x000001B390755400>}

# print(dir(Animal))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'say_hi']

# print(vars(Animal))
# {'__module__': '__main__', '__init__': <function Animal.__init__ at 0x000001FCA6C182C0>,
# 'say_hi': <function Animal.say_hi at 0x000001FCA6C23420>, '__dict__': <attribute '__dict__' of 'Animal' objects>,
# '__weakref__': <attribute '__weakref__' of 'Animal' objects>, '__doc__': None}

# print(dir(animal_object))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'age', 'name', 'say_hi']


# print(vars(animal_object))
# {'name': 'weirdo', 'age': 1}

# print(dir(Dog))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bark', 'say_hi']

# print(vars(Dog))
# {'__module__': '__main__', '__init__': <function Dog.__init__ at 0x0000019EC8DA3240>,
# 'bark': <function Dog.bark at 0x0000019EC8E3CA40>, '__doc__': None}


# print(dir(gaston))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'age', 'bark', 'breed', 'name', 'say_hi']

# print(vars(gaston))
# {'name': 'gaston', 'age': 4, 'breed': 'British Gaston'}



# print(dir(object))

