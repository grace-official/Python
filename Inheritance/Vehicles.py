class Vehicle:

    def __init__(self, numWheels, numPassengers):
        self.numWheels = numWheels
        self.numPassengers = numPassengers


class Car(Vehicle):

    def __init__(self, numPassengers):
        super().__init__(4, numPassengers)

class Motorcycle(Vehicle):

    def __init__(self):
        super().__init__(2, 1)

car = Car(5)
motorcycle = Motorcycle()

car.honkHorn()
motorcycle.maxLeanAmount()
