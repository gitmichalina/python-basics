class Animal:
    def __init__(self, name, sex, habitat):
        self.name = name
        self.sex = sex
        self.habitat = habitat


class Bird(Animal):
    unique_feature = "Feathers"


class Eagle(Bird):
    def fly(self):
        print("The eagle is flying")


class Penguin(Bird):
    def swim(self):
        print("The penguin is swimming")
