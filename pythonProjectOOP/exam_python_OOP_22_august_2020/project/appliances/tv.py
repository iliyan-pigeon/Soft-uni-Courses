from exam_python_OOP_22_august_2020.project.appliances.appliance import Appliance


class TV(Appliance):
    DAILY_COST = 1.5

    def __init__(self):
        super().__init__(TV.DAILY_COST)

