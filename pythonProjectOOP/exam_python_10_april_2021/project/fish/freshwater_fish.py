from exam_python_10_april_2021.project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    def eat(self):
        single_increase_amount = 3

        self.size += single_increase_amount

