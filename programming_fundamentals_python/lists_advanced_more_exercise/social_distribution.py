population_stats = [int(person) for person in input().split(", ")]
minimum_wealth = int(input())
if len(population_stats) * minimum_wealth > sum(population_stats):
    print("No equal distribution possible")
else:
    for person in range(len(population_stats)):
        if population_stats[person] < minimum_wealth:
            to_distribute = minimum_wealth - population_stats[person]
            wealthiest = population_stats.index(max(population_stats))
            population_stats[wealthiest] -= to_distribute
            population_stats[person] += to_distribute
    print(population_stats)
