class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )
#
#
# my_circle = Circle(4)
# my_circle.radius = 8
# print(my_circle.radius)
# del my_circle.radius
# help(my_circle)
#
# class Dog:
#     def __init__(self, name):
#         self._name = name
#     name = property(lambda self: self._name)
#
#
# dog = Dog("Gaston")
# print(dog.name)
#
print(Circle.radius.fget)
print(Circle.radius.fset)
print(Circle.radius.fdel)
print(dir(Circle.radius))
