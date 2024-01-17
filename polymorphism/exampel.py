class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print("Starting engine...")
        self._started = True

    def stop(self):
        print("Stopping engine...")
        self._started = False


class Car(Vehicle):
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year)
        self.num_seats = num_seats

    def drive(self):
        print(f'Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def drive(self):
        print(f'Riding my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_wheels} wheels'


toyota = Car("Toyota", "Corolla", 2022, 5)
honda = Car("Honda", "Civic", 2022, 4)
harley = Motorcycle("Harley-Davidson", "Iron 883", 2022, 2)
indian = Motorcycle("Indian", "Scout", 2022, 2)

for vehicle in [toyota, honda, harley, indian]:
    vehicle.drive()

# Driving my "Toyota - Corolla" on the road
# Driving my "Honda - Civic" on the road
# Riding my "Harley-Davidson - Iron 883" on the road
# Riding my "Indian - Scout" on the road
