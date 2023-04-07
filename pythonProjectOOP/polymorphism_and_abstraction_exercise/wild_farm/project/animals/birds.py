from polymorphism_and_abstraction_exercise.wild_farm.project.animals.animal import Bird


class Owl(Bird):
    WEIGHT_PER_PEACE_FOOD = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if type(food) != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += (Owl.WEIGHT_PER_PEACE_FOOD * food.quantity)


class Hen(Bird):
    WEIGHT_PER_PEACE_FOOD = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += (Hen.WEIGHT_PER_PEACE_FOOD * food.quantity)