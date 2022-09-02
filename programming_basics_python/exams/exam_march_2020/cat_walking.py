minutes_per_walk = int(input())
number_of_walks = int(input())
calories_per_day = int(input())
calories_per_minute = 5
minutes_per_day = minutes_per_walk * number_of_walks
burned_calories = minutes_per_day * calories_per_minute
minimum_burned_calories = calories_per_day * 0.5
if burned_calories >= minimum_burned_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
elif burned_calories < minimum_burned_calories:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
