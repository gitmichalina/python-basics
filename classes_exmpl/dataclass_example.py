from dataclasses import dataclass, astuple


@dataclass
class Point:
    x: int
    y: int
    z: int = 0

    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 4D Point!")

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)


my_point_1 = Point(1, 2, 3)
my_point_2 = Point(1, 2, 3)
print(repr(my_point_1))
# Point(x=1, y=2, z=3)
print(my_point_1 == my_point_2)
# True
print(astuple(my_point_1))
# (1, 2, 3)
