from exam_python_OOP_22_august_2020.project.appliances.appliance import Appliance
from exam_python_OOP_22_august_2020.project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        current_expenses = 0

        for arg in args:
            for element in arg:
                if isinstance(element, Appliance):
                    current_expenses += element.get_monthly_expense()
                elif isinstance(element, Child):
                    current_expenses += element.cost * 30

        self.expenses = current_expenses
