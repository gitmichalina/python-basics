class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.awake = False
        self.speed = 0
        self.max_speed = 50

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

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

    def __str__(self):
        return f"Person name is {self.name} and is {self.age} years old."

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"\nname='{self._name}'"
            f"\nage={self._age}"
        )

    @classmethod
    def from_list(cls, lst):
        return (cls(*lst))

    @staticmethod
    def show_intro_message():
        print("siemka")


list_with_arg = ["Misia", 45]
new_person = Person.from_list(list_with_arg)
print(new_person)
# Person name is Misia and is 45 years old.

Person.show_intro_message()
my_person = Person("Misia", 33)
my_person.show_intro_message()

print(repr(my_person))
# Person
# name='Misia'
# age=33

print(str(my_person))
# Person name is Misia and is 33 years old.

# Person
# name='Misia'
# age=33
# Person name is Misia and is 33 years old.
