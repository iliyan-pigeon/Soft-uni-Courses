from encapsulation_exercise.restaurant.project.food.food import Food


class Starter(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)