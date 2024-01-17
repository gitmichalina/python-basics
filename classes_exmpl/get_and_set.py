class Person:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value


my_person = Person("Jane")
my_person.get_name()
my_person.set_name("New Jane")