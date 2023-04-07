from exam_python_10_april_2021.project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    def eat(self):
        single_increase_amount = 2

        self.size += single_increase_amount

