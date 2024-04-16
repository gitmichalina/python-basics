class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    # def speak(self, sound="default terrier sound"):
    #     return f"{self.name} says {sound}"

    def speak(self, sound="default terrier sound"):
        return super().speak(sound)


dog = Dog("some doggo", 4)
ter = JackRussellTerrier("terrier", 4)

print(dog.speak("dogggooo"))
print(ter.speak())
