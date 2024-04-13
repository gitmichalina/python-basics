class Animal:

    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print(self.name, 'Animal is constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


class Dog(Animal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)


stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))

print(type(open))

