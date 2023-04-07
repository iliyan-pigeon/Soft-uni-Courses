from exam_python_10_april_2021.project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 50)

    def calculate_comfort(self):
        decorations_comfort_combined = sum([d.comfort for d in self.decorations])

        return decorations_comfort_combined

    def add_fish(self, fish):
        possible_fish_types = ["FreshwaterFish"]

        if fish.__type__.__name__ in possible_fish_types:
            if len(self.fish) == self.capacity:
                return "Not enough capacity."

            self.fish.append(fish)

            return f"Successfully added {fish.__type__.__name__} to {self.__name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        if not self.fish:
            fishes = "none"
        else:
            fishes = ' '.join(self.fish)

        result = f'"{self.name}:\n' \
                 f'Fish: {fishes}\n' \
                 f'Decorations: {len(self.decorations)}\n' \
                 f'Comfort: {self.calculate_comfort()}'

        return result
