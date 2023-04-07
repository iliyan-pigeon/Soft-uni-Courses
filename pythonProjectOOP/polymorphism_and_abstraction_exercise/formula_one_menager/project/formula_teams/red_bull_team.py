from polymorphism_and_abstraction_exercise.formula_one_menager.project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        revenue = 0

        if race_pos == 10:
            revenue += 10000
        elif race_pos == 8:
            revenue += 20000
        elif race_pos == 2:
            revenue += 800000 + 20000
        elif race_pos == 1:
            revenue += 1500000 + 20000

        revenue -= self.EXPENSES_PER_RACE

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
