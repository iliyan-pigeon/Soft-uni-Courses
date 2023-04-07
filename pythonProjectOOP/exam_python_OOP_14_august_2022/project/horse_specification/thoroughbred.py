from exam_python_OOP_14_august_2022.project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    IMPROVEMENT_AFTER_TRAINING = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.IMPROVEMENT_AFTER_TRAINING > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.IMPROVEMENT_AFTER_TRAINING
