from encapsulation_exercise.pizza_maker.project.dough import Dough
from encapsulation_exercise.pizza_maker.project.topping import Topping

class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping):
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        if self.__toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = sum(value for key, value in self.toppings.items()) + self.__dough.weight
        return total_weight


d = Dough("Sugar", "Mixing", 20)
t = Topping("Tomato", 20)
p = Pizza("Burger", d, 200)
p.add_topping(t)
p.add_topping(t)
p.calculate_total_weight()



