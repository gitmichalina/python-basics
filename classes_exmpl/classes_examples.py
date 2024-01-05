class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('Hello', self.name)


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('Hello', self.name)


class TheSamePerson(object):
    name = "Joe"
    age = 23

    def say_hi(self):
        print("Hello Joe")

    def get_older(self):
        self.age += 1

    def get_much_older(self, years):
        for i in range(0, years):
            self.get_older()


class Friend(Person):

    def __str__(self):
        return self.name + "'s age is " + str(self.age)
    def __init__(self, name, age, nick):
        super().__init__(name, age)
        self.nickname = nick

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass




    def smile(self):
        print("smiling")

    def say_hi(self, extra):
        super().say_hi()
        print(extra)




def main():
    my_person = Person("Marta", 35)
    my_person.say_hi()

    my_person.name = "Misia"

    my_person.dog = "Gaston"

    meg = Person('Margaret', 25)
    bob = Friend('Robert', 33, "niuniek")

    my_friend = Friend("Gaston", 43, "niuniek")
    my_friend.say_hi("tutaj extra treść")

    print(str(my_friend))
    print(repr(my_friend))




main()

