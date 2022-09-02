kilos_food = int(input())
current_food_grams = input()
difference = 0
eaten_food = 0
grams_food = kilos_food * 1000
while current_food_grams != "Adopted":
    grams_eaten = int(current_food_grams)
    eaten_food += grams_eaten
    current_food_grams = input()
difference = abs(eaten_food - grams_food)
if eaten_food <= grams_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
elif eaten_food > grams_food:
    print(f"Food is not enough. You need {difference} grams more.")