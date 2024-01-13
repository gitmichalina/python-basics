def main():
    person1 = Person(21)
    person2 = Person(22)

    print(person1 + person2)


class Person():
    def __init__(self, age):
        self.age = age

    def __add__(self, other):
        return self.age + other.age


if __name__ == '__main__':
    main()
