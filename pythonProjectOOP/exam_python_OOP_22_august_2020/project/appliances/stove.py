from exam_python_OOP_22_august_2020.project.appliances.appliance import Appliance


class Stove(Appliance):
    DAILY_COST = 0.7

    def __init__(self):
        super().__init__(Stove.DAILY_COST)

