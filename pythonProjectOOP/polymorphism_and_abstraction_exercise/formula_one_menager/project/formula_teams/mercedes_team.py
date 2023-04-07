from polymorphism_and_abstraction_exercise.formula_one_menager.project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        revenue = 0

        if race_pos == 7:
            revenue += 50000
        elif race_pos == 5:
            revenue += 100000
        elif race_pos == 3:
            revenue += 500000 + 100000
        elif race_pos == 1:
            revenue += 1000000 + 100000

        revenue -= self.EXPENSES_PER_RACE

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
