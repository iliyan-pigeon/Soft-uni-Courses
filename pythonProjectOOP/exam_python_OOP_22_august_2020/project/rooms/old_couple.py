from exam_python_OOP_22_august_2020.project.appliances.fridge import Fridge
from exam_python_OOP_22_august_2020.project.appliances.stove import Stove
from exam_python_OOP_22_august_2020.project.appliances.tv import TV
from exam_python_OOP_22_august_2020.project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        budget = pension_one + pension_two
        super().__init__(family_name, budget, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)
