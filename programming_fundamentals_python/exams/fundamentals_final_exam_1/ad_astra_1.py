import re


def extract_data(sentence: str):
    pattern = r"(\#|\|)([A-Z][a-z ?A-Z?]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,})\1"
    extracted_data = re.findall(pattern, sentence)
    total_calories = 0
    needed_daily_calories = 2000
    for food in extracted_data:
        total_calories += int(food[3])
    surviving_days = total_calories // needed_daily_calories
    to_return = f"You have food to last you for: {surviving_days} days!\n"
    for food in extracted_data:
        to_return += f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}\n"
    return to_return


characters = input()
print(extract_data(characters))
