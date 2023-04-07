from polymorphism_and_abstraction_exercise.formula_one_menager.project.formula_teams.red_bull_team import RedBullTeam
from polymorphism_and_abstraction_exercise.formula_one_menager.project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name, budget):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
            return f"{team_name} has joined the new F1 season."
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
            return f"{team_name} has joined the new F1 season."

        raise ValueError("Invalid team name!")

    def new_race_results(self, race_name, red_bull_pos, mercedes_pos):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        if red_bull_pos > mercedes_pos:
            return f"Red Bull: {RedBullTeam.calculate_revenue_after_race(self.red_bull_team, red_bull_pos)}. " \
                   f"Mercedes: {MercedesTeam.calculate_revenue_after_race(self.mercedes_team, mercedes_pos)}. " \
                   f"Mercedes is ahead at the {race_name} race."
        elif red_bull_pos < mercedes_pos:
            return f"Red Bull: {RedBullTeam.calculate_revenue_after_race(self.red_bull_team, red_bull_pos)}. " \
                   f"Mercedes: {MercedesTeam.calculate_revenue_after_race(self.mercedes_team, mercedes_pos)}. " \
                   f"Red Bull is ahead at the {race_name} race."
