from exam_puthon_actual_10_december_2022.project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float, portion=200):
        super().__init__(name, portion, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
