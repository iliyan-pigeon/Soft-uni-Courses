from encapsulation_exercise.restaurant.project.beverage.beverage import Beverage


class HotBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
