import random


class Hat:
    houses = ["kraków", "Warszawa"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))




Hat.sort("Misia")