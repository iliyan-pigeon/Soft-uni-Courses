import math

days_away = int(input())
food_left_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())
total_dog_food = dog_food_per_day_kg * days_away
total_cat_food = cat_food_per_day_kg * days_away
total_turtle_food = (turtle_food_per_day_g / 1000) * days_away
total_food_kg = total_dog_food + total_cat_food + total_turtle_food
difference = abs(total_food_kg - food_left_kg)
if total_food_kg <= food_left_kg:
    print(f"{math.floor(difference)} kilos of food left.")
elif total_food_kg > food_left_kg:
    print(f"{math.ceil(difference)} more kilos of food are needed.")