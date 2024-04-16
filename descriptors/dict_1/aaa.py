class Vehicle():
    can_fly = False
    number_of_wheels = 0


class Car(Vehicle):
    number_of_wheels = 4

    def __init__(self, color):
        self.color = color


my_car = Car("red")
print(my_car.__dict__)
print(type(my_car).__dict__)
print(Car.__dict__)