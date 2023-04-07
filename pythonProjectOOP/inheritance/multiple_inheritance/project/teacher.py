from encapsulation_exercise.wild_cat_zoo.project import Employee
from encapsulation_exercise.wild_cat_zoo.project import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


