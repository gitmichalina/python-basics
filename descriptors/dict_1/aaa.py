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

print(my_car.color)
print(my_car.number_of_wheels)
print(my_car.can_fly)


print(my_car.__dict__['color'])
print(type(my_car).__dict__['number_of_wheels'])
print(type(my_car).__base__.__dict__['can_fly'])