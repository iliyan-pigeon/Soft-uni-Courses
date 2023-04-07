from exam_python_OOP_22_august_2020.project.appliances.fridge import Fridge
from exam_python_OOP_22_august_2020.project.appliances.laptop import Laptop
from exam_python_OOP_22_august_2020.project.appliances.tv import TV
from exam_python_OOP_22_august_2020.project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        budget = salary_two + salary_one
        number_of_people = 2 + len(children)
        super().__init__(family_name, budget, number_of_people)
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * number_of_people
        self.calculate_expenses(self.appliances, self.children)
