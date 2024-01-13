def main():
    person = Person("misia", 23, "male")
    print(person.name)
    print(person.age)
class Person():
    def __init__(self, name, age, gender):
        self.__age = age
        self.name = name
        self._gender = gender

    def __add__(self, other):
        return self.age + other.age


if __name__ == '__main__':
    main()