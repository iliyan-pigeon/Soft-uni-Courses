from exam_python_OOP_22_august_2020.project.appliances.appliance import Appliance


class Laptop(Appliance):
    DAILY_COST = 1

    def __init__(self):
        super().__init__(Laptop.DAILY_COST)

