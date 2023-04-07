from exam_python_23_august_2021.project.astronaut.astronaut_repository import AstronautRepository
from exam_python_23_august_2021.project.astronaut.biologist import Biologist
from exam_python_23_august_2021.project.astronaut.geodesist import Geodesist
from exam_python_23_august_2021.project.astronaut.meteorologist import Meteorologist
from exam_python_23_august_2021.project.planet.planet import Planet
from exam_python_23_august_2021.project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        the_astronaut = self.astronaut_repository.find_by_name(name)
        if the_astronaut is not None:
            return f"{name} is already added."

        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
            self.astronaut_repository.add(astronaut)

            return f"Successfully added {astronaut_type}: {name}."

        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
            self.astronaut_repository.add(astronaut)

            return f"Successfully added {astronaut_type}: {name}."

        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)
            self.astronaut_repository.add(astronaut)

            return f"Successfully added {astronaut_type}: {name}."

        else:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        the_planet = self.planet_repository.find_by_name(name)
        if the_planet is not None:
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")

        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        the_astronaut = self.astronaut_repository.find_by_name(name)
        if the_astronaut:
            self.astronaut_repository.remove(the_astronaut)
            return f"Astronaut {name} was retired!"

        return f"Astronaut {name} doesn't exist!"

    def recharge_oxygen(self):
        recharging_amount = 10

        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(recharging_amount)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception("Invalid planet name!")

        capable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        if not capable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        while len(capable_astronauts) > 5:
            lowest_oxygen = min([a.oxygen for a in capable_astronauts])
            least_capable_astronaut = [a for a in capable_astronauts if a.oxygen == lowest_oxygen][0]

            capable_astronauts.remove(least_capable_astronaut)

        hierarchy_ordered_astronauts = sorted(capable_astronauts, key=lambda x: x.oxygen, reverse=True)

        participating_astronauts = 0
        for astronaut in hierarchy_ordered_astronauts:
            while planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                if astronaut.oxygen <= 0:
                    break
            participating_astronauts += 1
            if not planet.items:
                break

        if not planet.items:
            self.successful_missions += 1

            return f"Planet: {planet_name} was explored. {participating_astronauts}" \
                   f" astronauts participated in collecting items."

        self.failed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.successful_missions} successful missions!",
                  f"{self.failed_missions} missions were not completed!", "Astronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")

            if not astronaut.backpack:
                result.append('Backpack items: none')
            else:
                result.append(f"Backpack items: {', '.join(astronaut.backpack)}")

        return '\n'.join(result)

