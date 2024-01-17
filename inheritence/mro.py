class GrandMother:
    def method(self):
        print("GrandMother.method")


class Mother(GrandMother):
    def method(self):
        print("Mother.method")


class Father(GrandMother):
    def method(self):
        print("Father.method")


class Kid1(Mother, Father):
    pass


class Kid2(Father, Mother):
    pass


kid = Kid1()
kid.method()
# Mother.method
kid = Kid2()
kid.method()
# Father.method

print(Kid1.__mro__)
# (<class '__main__.Kid1'>, <class '__main__.Mother'>, <class '__main__.Father'>,
# <class '__main__.GrandMother'>, <class 'object'>)
print(Kid2.__mro__)
# (<class '__main__.Kid2'>, <class '__main__.Father'>, <class '__main__.Mother'>,
# <class '__main__.GrandMother'>, <class 'object'>)
