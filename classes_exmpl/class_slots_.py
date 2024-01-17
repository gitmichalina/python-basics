from pympler import asizeof


class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


new_point = Point(1, 2)
# print(vars(new_point))
# TypeError: vars() argument must have __dict__ attribute

new_point.z = 65454
# AttributeError: 'Point' object has no attribute 'z'


print(asizeof.asizeof(Point(1, 2)))
# 112


class PointWithInit:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print(asizeof.asizeof(PointWithInit(1, 2)))
# 504