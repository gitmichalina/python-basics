# point.py

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        raise WriteCoordinateError("x coordinate is read-only")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        raise WriteCoordinateError("y coordinate is read-only")


point = Point(1, 2)
point.x = 1
# AttributeError: property 'x' of 'Point' object has no setter
point.y = 2
# AttributeError: property 'y' of 'Point' object has no setter
