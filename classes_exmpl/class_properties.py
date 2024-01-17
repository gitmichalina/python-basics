class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.awake = False
        self.speed = 0
        self.max_speed = 50

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("positive number expected")
        self._age = value

    def wake_up(self):
        print("Good morning@")
        self.awake = True

    def accelerate(self, value):
        if not self.awake:
            print("Person is still sleeping!")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
            print("Person is walking")
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h...")

    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f"Braking to {self.speed} km/h...")
        else:
            self.speed = 0
            self.go_to_sleep()

    def go_to_sleep(self):
        print("Person is falling asleep...")
        self.awake = True


my_person = Person("Misia", 33)
print(vars(my_person))
my_person.wake_up()
my_person.accelerate(20)
my_person.accelerate(80)
my_person.brake(2)
my_person.brake(34)
my_person.brake(90)


# Good morning
# Person is walking
# Accelerating to 20 km/h...
# Accelerating to 50 km/h...
# Braking to 48 km/h...
# Braking to 14 km/h...
# Person is falling asleep...

Person.wake_up(my_person)
# Good morning@