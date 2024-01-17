class Person:
    def __init__(self, name, age):
        # calling setters
        self.name = name
        self.age = age

    @classmethod
    def get_person(cls, name, age):
        return cls(name, age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("Invalid age")
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name not in ["Misia", "Marta"]:
            raise ValueError("Invalid name")
        self._name = name

    def __str__(self):
        return f'{self.name} is {self.age} years'


# person = Person("Misia", 14)
# person.age = 20
# print(person)
# person.name = "Koko"

Person.get_person("Koko", 15)
