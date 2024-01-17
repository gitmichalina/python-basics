class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("positive number expected!")
        instance.__dict__[self._name] = value


class Person:
    age = PositiveNumber()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value


my_person = Person("Misia", 0)
print(vars(my_person))
