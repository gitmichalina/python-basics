# stuff = list()
# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
# print(stuff[0])
# print(stuff.__getitem__(0))
# print(list.__getitem__(stuff, 0))


class PartyAnimal:

   def __init__(self):
     self.x = 0
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

animal_obj = PartyAnimal()
# an.party()
# an.party()
# print(vars(animal_obj))
# print(dir(animal_obj))
# print(vars(PartyAnimal))
# print(dir(PartyAnimal))
# print(dir())