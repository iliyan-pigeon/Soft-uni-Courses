from exam_python_11_december_2021.project.car.muscle_car import MuscleCar
from exam_python_11_december_2021.project.car.sports_car import SportsCar
from exam_python_11_december_2021.project.driver import Driver
from exam_python_11_december_2021.project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type == "MuscleCar":
            if model in [c.model for c in self.cars if c.__class__.__name__ == "MuscleCar"]:
                raise Exception(f"Car {model} is already created!")

            car = MuscleCar(model, speed_limit)
            self.cars.append(car)

            return f"{car_type} {model} is created."

        elif car_type == "SportsCar":
            if model in [c.model for c in self.cars if c.__class__.__name__ == "SportsCar"]:
                raise Exception(f"Car {model} is already created!")

            car = SportsCar(model, speed_limit)
            self.cars.append(car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = [d for d in self.drivers if d.name == driver_name]

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = driver[0]

        car = ''
        for c in self.cars:
            if c.__class__.__name__ == car_type and not c.is_taken:
                car = c

        if car == '':
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is None:
            car.is_taken = True
            driver.car = car

            return f"Driver {driver_name} chose the car {car.model}."

        elif driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False
            car.is_taken = True
            driver.car = car

            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = [r for r in self.races if r.name == race_name]

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        race = race[0]

        driver = [d for d in self.drivers if d.name == driver_name]

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = driver[0]

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver_name in [d.name for d in race.drivers]:
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        race = race[0]

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_drivers = []
        while len(fastest_drivers) != 3:
            winner_speed = max([d.car.speed_limit for d in race.drivers])
            winner = [d for d in race.drivers if d.car.speed_limit == winner_speed][0]
            winner.number_of_wins += 1
            fastest_drivers.append(winner)
            race.drivers.remove(winner)

        result = ''
        for d in fastest_drivers:
            race.drivers.append(d)
            if d == fastest_drivers[-1]:
                result += f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}."
            else:
                result += f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.\n"

        return result
