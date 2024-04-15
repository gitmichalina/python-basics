# circle.py

from functools import cached_property
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(0.5)  # Simulate a costly computation
        return self.radius * 2


circle = Circle(42.0)
print(circle.diameter)  # With delay
# 84.0

print(circle.diameter)  # Without delay
# 84.0

circle.radius = 100
print(circle.diameter)  # Wrong diameter
# 84.0

# Allow direct assignment
circle.diameter = 200
print(circle.diameter)  # Cached value
# 200