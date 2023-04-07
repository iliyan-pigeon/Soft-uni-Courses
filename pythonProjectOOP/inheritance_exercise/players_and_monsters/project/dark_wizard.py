from encapsulation_exercise.wild_cat_zoo.project import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)