from exam_python_11_december_2021.project.car.car import Car


class MuscleCar(Car):
    MIN_LIMIT = 250
    MAX_LIMIT = 450

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

