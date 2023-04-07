from exam_python_OOP_15_august_2021.project.baked_food.baked_food import BakedFood
from exam_python_OOP_15_august_2021.project.drink.drink import Drink
from exam_python_OOP_15_august_2021.project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__capacity

    @table_number.setter
    def table_number(self, value):
        if value < 1 or value > 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")

        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        drinks_sum = sum(drink.price for drink in self.drink_orders)
        foods_sum = sum(baked_food.price for baked_food in self.food_orders)
        total_sum = drinks_sum + foods_sum

        return total_sum

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"

            return result
