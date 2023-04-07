from exam_python_OOP_10_april_2022.project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy=25):
        super().__init__(name, energy)

    def details(self):
        return f"Food: {self.name}, {self.energy}"

