import re

products_data = input()
searched_pattern = r"(\#|\|)([A-Z][a-z ?A-Z?]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,})\1"
needed_calories_per_day = 2000
filtered_data = re.findall(searched_pattern, products_data)
total_calories = 0
for food in filtered_data:
    total_calories += int(food[3])
surviving_days = total_calories // needed_calories_per_day
print(f"You have food to last you for: {surviving_days} days!")
for food in filtered_data:
    print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}")
