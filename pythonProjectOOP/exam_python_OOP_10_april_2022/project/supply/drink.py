from exam_python_OOP_10_april_2022.project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str, energy=15):
        super().__init__(name, energy)

    def details(self):
        return f"Drink: {self.name}, {self.energy}"
