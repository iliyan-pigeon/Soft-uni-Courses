from encapsulation_exercise.wild_cat_zoo.project import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)