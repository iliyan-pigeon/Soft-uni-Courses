from exam_python_OOP_22_august_2020.project.appliances.appliance import Appliance


class Fridge(Appliance):
    DAILY_COST = 1.2

    def __init__(self):
        super().__init__(Fridge.DAILY_COST)

