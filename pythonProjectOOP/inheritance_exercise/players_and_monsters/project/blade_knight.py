from encapsulation_exercise.wild_cat_zoo.project import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)