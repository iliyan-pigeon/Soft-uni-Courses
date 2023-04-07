from exam_python_OOP_14_august_2022.project.horse_race import HorseRace
from exam_python_OOP_14_august_2022.project.horse_specification.appaloosa import Appaloosa
from exam_python_OOP_14_august_2022.project.horse_specification.thoroughbred import Thoroughbred
from exam_python_OOP_14_august_2022.project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [horse.name for horse in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in HorseRaceApp.VALID_HORSE_TYPES:

            horse = HorseRaceApp.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, jockey_age: int):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, jockey_age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [race.race_type for race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = [jockey for jockey in self.jockeys if jockey.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = jockey[0]

        horse = [horse for horse in self.horses if horse.__class__.__name__ == horse_type and not horse.is_taken]
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        horse = horse[-1]

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = [race for race in self.horse_races if race.race_type == race_type]
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        race = race[0]

        jockey = [jockey for jockey in self.jockeys if jockey.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = jockey[0]
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey_name in [jockey.name for jockey in race.jockeys]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = [race for race in self.horse_races if race.race_type == race_type]
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        race = race[0]
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_speed = 0
        winner = ''
        for jockey in race.jockeys:
            if jockey.horse.speed > winner_speed:
                winner_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {winner_speed}km/h" \
               f" is {winner.name}! Winner's horse: {winner.horse.name}."
