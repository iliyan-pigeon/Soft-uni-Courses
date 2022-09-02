food_string = input()
food_data = {}
needed_calories_daily = 2000
record = False
sign = ""
product = ""
date = ""
calories = ""
total_calories = 0
for symbol in food_string:
    if record:
        if "#" in sign:
            if len(sign) == 1 and symbol.isalpha():
                product += symbol
            elif len(sign) == 2 and symbol.isnumeric() or symbol == "/":
                date += symbol
            elif len(sign) == 3 and symbol.isnumeric():
                calories += symbol
            elif len(sign) == 1 and symbol == "#":
                sign += "#"
            elif len(sign) == 2 and symbol == "#":
                sign += "#"
            elif len(sign) == 3 and symbol == "#":
                food_data[product] = {}
                food_data[product]["date"] = date
                food_data[product]["calories"] = int(calories)
                total_calories += int(calories)
                record = False
                product = ""
                date = ""
                calories = ""
                sign = ""
                continue
            else:
                product = ""
                date = ""
                calories = ""
                sign = ""
                record = False
                continue
        elif "|" in sign:
            if len(sign) == 1 and symbol.isalpha():
                product += symbol
            elif len(sign) == 2 and symbol.isnumeric() or symbol == "/":
                date += symbol
            elif len(sign) == 3 and symbol.isnumeric():
                calories += symbol
            elif len(sign) == 1 and symbol == "|":
                sign += "#"
            elif len(sign) == 2 and symbol == "|":
                sign += "#"
            elif len(sign) == 3 and symbol == "|":
                food_data[product] = {}
                food_data[product]["date"] = date
                food_data[product]["calories"] = int(calories)
                total_calories += int(calories)
                record = False
                product = ""
                date = ""
                calories = ""
                sigh = ""
                continue
            else:
                product = ""
                date = ""
                calories = ""
                sigh = ""
                record = False
                continue
    if symbol == "#" and not record:
        record = True
        sign += "#"
    elif symbol == "|" and not record:
        record = True
        sign += "|"
lasting_days = total_calories // needed_calories_daily
print(f"You have food to last you for: {lasting_days} days!")
for food, info in food_data.items():
    date = ""
    calories = ""
    iteration = 0
    for key, value in info.items():
        iteration += 1
        if iteration == 1:
            date = value
            continue
        calories = str(value)
    print(f"Item: {food}, Best before: {date}, Nutrition: {calories}")



