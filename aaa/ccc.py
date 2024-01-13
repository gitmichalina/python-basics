def main():
    per1 = NewFriend("koko", 23, 3)
    print(per1)


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Friend(Person):
    def __init__(self, name, age, nick):
        super().__init__(name, age)
        self.nickname = nick


class NewFriend(Person):
    def __init__(self, name, age, weight):
        Person.__init__(self, name, age)
        self.weight = weight


if __name__ == '__main__':
    main()
