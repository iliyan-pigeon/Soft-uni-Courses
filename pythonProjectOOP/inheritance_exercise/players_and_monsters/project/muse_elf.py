from encapsulation_exercise.wild_cat_zoo.project import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)