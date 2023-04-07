from exam_python_23_august_2021.project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    UNITS_DECREASED = 5

    def __init__(self, name: str, oxygen=70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= Biologist.UNITS_DECREASED

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

