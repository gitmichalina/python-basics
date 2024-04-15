# persons.py

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Person implementation...


class Employee(Person):
    @property
    def name(self):
        return super().name.upper()

    # Employee implementation...


person = Person("John")
print(person.name)
person.name = "John Doe"
print(person.name)
employee = Employee("John")
print(employee.name)

employee.name = "John Doe"
# AttributeError: property 'name' of 'Employee' object has no setter
