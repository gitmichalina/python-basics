from enum import Enum


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def favorite_day(cls):
        return cls.FRIDAY

    def __str__(self):
        return f"Current day: {self.name}"


# WeekDay.FRIDAY = 6
# AttributeError: cannot reassign member 'FRIDAY'
print(list(WeekDay))
# [<WeekDay.MONDAY: 1>, <WeekDay.TUESDAY: 2>, <WeekDay.WEDNESDAY: 3>, <WeekDay.THURSDAY: 4>,
# <WeekDay.FRIDAY: 5>, <WeekDay.SATURDAY: 6>, <WeekDay.SUNDAY: 7>]

print(WeekDay.MONDAY)
print(WeekDay(2))
print(WeekDay["WEDNESDAY"])

# WeekDay.MONDAY
# WeekDay.TUESDAY
# WeekDay.WEDNESDAY

print(WeekDay.THURSDAY.name)
# THURSDAY
print(WeekDay.FRIDAY.value)
# 5

print(WeekDay.FRIDAY)
# Current day: FRIDAY

for day in WeekDay:
    print(day.name, "->", day.value, end=" ")
# MONDAY -> 1 TUESDAY -> 2 WEDNESDAY -> 3 THURSDAY -> 4 FRIDAY -> 5 SATURDAY -> 6 SUNDAY -> 7
