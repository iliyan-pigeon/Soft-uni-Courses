from encapsulation_exercise.wild_cat_zoo.project import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)