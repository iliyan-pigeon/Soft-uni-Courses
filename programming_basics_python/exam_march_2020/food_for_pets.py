days_number = int(input())
amount_food = float(input())
dog_food = 0
cat_food = 0
combined_food = 0
percent_eaten_food = 0
biscuits_total = 0
percent_dog = 0
percent_cat = 0
for day in range(1, days_number + 1):
    current_dog_food = int(input())
    current_cat_food = int(input())
    dog_food += current_dog_food
    cat_food += current_cat_food
    if day % 3 == 0:
        biscuits = (current_dog_food + current_cat_food) * 0.1
        biscuits_total += biscuits
combined_food = dog_food + cat_food
percent_eaten_food = combined_food / amount_food * 100
percent_dog = dog_food / combined_food * 100
percent_cat = cat_food / combined_food * 100
print(f"Total eaten biscuits: {round(biscuits_total)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")