from encapsulation_exercise.wild_cat_zoo.project import Animal


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)