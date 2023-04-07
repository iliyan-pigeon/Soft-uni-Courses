from exam_python_23_august_2021.project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name: str, oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= Geodesist.UNITS_DECREASED

    def increase_oxygen(self, amount: int):
        self.oxygen += amount



