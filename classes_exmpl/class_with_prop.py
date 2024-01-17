class Person:
    def __init__(self, name):
        self.name = name


class NewPerson:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()
