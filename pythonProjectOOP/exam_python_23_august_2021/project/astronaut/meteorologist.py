from exam_python_23_august_2021.project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNITS_DECREASED = 15

    def __init__(self, name: str, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= Meteorologist.UNITS_DECREASED

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

