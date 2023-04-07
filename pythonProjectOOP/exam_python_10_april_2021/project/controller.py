from exam_python_10_april_2021.project.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam_python_10_april_2021.project.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam_python_10_april_2021.project.decoration.decoration_repository import DecorationRepository
from exam_python_10_april_2021.project.decoration.ornament import Ornament
from exam_python_10_april_2021.project.decoration.plant import Plant
from exam_python_10_april_2021.project.fish.freshwater_fish import FreshwaterFish
from exam_python_10_april_2021.project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]

        if aquarium_type not in valid_aquarium_types:
            return "Invalid aquarium type."

        aquarium = ''

        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)

        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_decoration_types = ["Ornament", "Plant"]

        if decoration_type not in valid_decoration_types:
            return "Invalid decoration type."

        decoration = ''

        if decoration_type == "Ornament":
            decoration = Ornament()

        elif decoration_type == "Plant":
            decoration = Plant()

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = [a for a in self.aquariums if a.name == aquarium_name]

        if aquarium:
            aquarium = aquarium[0]

        if aquarium != '':
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)

            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]

        if fish_type not in valid_fish_types:
            return f"There isn't a fish of type {fish_type}."

        fish = ''
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]

        if aquarium:
            aquarium = aquarium[0]

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)

            if type(aquarium).__name__ != "FreshwaterAquarium":
                return "Water not suitable."

        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)

            if type(aquarium).__name__ != "SaltwaterAquarium":
                return "Water not suitable."

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]

        if aquarium:
            aquarium = aquarium[0]
            aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        fish_value = sum([f.price for f in aquarium.fish])
        decoration_value = sum([d.price for d in aquarium.decoration])
        total_aquarium_value = fish_value + decoration_value

        return f"The value of Aquarium {aquarium_name} is {total_aquarium_value:.2f}."

    def report(self):
        result = '\n'.join(self.aquariums)

        return result
