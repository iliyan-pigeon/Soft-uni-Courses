from encapsulation_exercise.wild_cat_zoo.project import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


