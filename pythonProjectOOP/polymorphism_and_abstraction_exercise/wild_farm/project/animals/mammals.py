from polymorphism_and_abstraction_exercise.wild_farm.project.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_PER_PEACE_FOOD = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if type(food) != "Vegetable" and type(food) != "Fruit":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += (Mouse.WEIGHT_PER_PEACE_FOOD * food.quantity)


class Dog(Mammal):
    WEIGHT_PER_PEACE_FOOD = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if type(food) != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += (Dog.WEIGHT_PER_PEACE_FOOD * food.quantity)


class Cat(Mammal):
    WEIGHT_PER_PEACE_FOOD = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meaw"

    def feed(self, food):
        if type(food) != "Vegetable" and type(food) != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += (Cat.WEIGHT_PER_PEACE_FOOD * food.quantity)


class Tiger(Mammal):
    WEIGHT_PER_PEACE_FOOD = 1.00

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food) != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += (Tiger.WEIGHT_PER_PEACE_FOOD * food.quantity)
