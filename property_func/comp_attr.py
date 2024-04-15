class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    @property
    def price(self):
        return f"${self._price:,.2f}"


# point.py

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return round(math.dist((0, 0), (self.x, self.y)))

    @property
    def angle(self):
        return round(math.degrees(math.atan(self.y / self.x)), 1)

    def as_cartesian(self):
        return self.x, self.y

    def as_polar(self):
        return self.distance, self.angle


# circle.py

from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = None

    @property
    def diameter(self):
        if self._diameter is None:
            sleep(0.5)  # Simulate a costly computation
            self._diameter = self.radius * 2
        return self._diameter


circle = Circle(42.0)
print(circle.radius)

print(circle.diameter)  # With delay

print(circle.diameter)  # Without delay

circle.radius = 100.0
print(circle.diameter)  # Wrong diameter
