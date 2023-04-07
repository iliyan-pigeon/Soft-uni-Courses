from exam_python_OOP_22_august_2022.project.meals.meal import Meal


class Dessert(Meal):
    def __init__(self, name, price, quantity=30):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
