class Vehicle:

    def __init__(self, numWheels, numPassengers):
        self.numWheels = numWheels
        self.numPassengers = numPassengers

    def drive(self):
        print("Now driving")

    def changeNumPassengers(self, newMax):
        self.numPassengers = newMax

class Car(Vehicle):

    def __init__(self, numPassengers):
        super().__init__(4, numPassengers)

    def honkHorn(self):
        print("Honk honk")

class Motorcycle(Vehicle):

    def __init__(self):
        super().__init__(2, 1)
        self.leanAmount = 60

    def maxLeanAmount(self, maxLean):
        self.leanAmount = maxLean

car = Car(5)
motorcycle = Motorcycle()

print(car.numWheels)
print(motorcycle.numWheels)

car.drive()
motorcycle.drive()

car.changeNumPassengers(4)
motorcycle.changeNumPassengers(2)

car.honkHorn()
motorcycle.leanAmount
motorcycle.maxLeanAmount()
