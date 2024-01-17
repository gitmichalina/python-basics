class ObjectCounter:
    num_instances = 0

    def __init__(self):
        ObjectCounter.num_instances += 1
        # type(self).num_instances += 1


my_object = ObjectCounter()

print(ObjectCounter.num_instances)
# 1
print(my_object.num_instances)
# 1
print(vars(my_object))
# {}
my_object.num_instances = 9
print(my_object.num_instances)
# 9
print(vars(my_object))
# {'num_instances': 9}
print(ObjectCounter.num_instances)
# 1
ObjectCounter.num_instances = 4
print(ObjectCounter.num_instances)
# 4

ObjectCounter.hoho = "nonoo"
print(vars(ObjectCounter))


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200



class Record:
    """Hold a record of data."""



