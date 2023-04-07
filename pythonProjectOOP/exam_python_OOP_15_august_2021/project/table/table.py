from abc import ABC, abstractmethod
from exam_python_OOP_15_august_2021.project.baked_food.baked_food import BakedFood
from exam_python_OOP_15_august_2021.project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    @abstractmethod
    def order_food(self, baked_food: BakedFood):
        pass

    @abstractmethod
    def order_drink(self, drink: Drink):
        pass

    @abstractmethod
    def get_bill(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def free_table_info(self):
        pass
