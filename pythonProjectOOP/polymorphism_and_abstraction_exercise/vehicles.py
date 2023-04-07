from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    AIR_CONDITION_0N = 0.9

    def drive(self, distance):
        consumption = (self.fuel_consumption + Car.AIR_CONDITION_0N) * distance
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITION_ON = 1.6

    def drive(self, distance):
        consumption = (self.fuel_consumption + Truck.AIR_CONDITION_ON) * distance
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)




