import math

people_number = int(input())
entry_tax = float(input())
sunbed_price = float(input())
umbrella_price = float(input())
entry_price = entry_tax * people_number
umbrellas_number = math.ceil(people_number / 2)
umbrellas_price = umbrellas_number * umbrella_price
sunbeds_number = math.ceil(people_number * 0.75)
sunbeds_price = sunbeds_number * sunbed_price
total_price = entry_price + umbrellas_price + sunbeds_price
print(f"{total_price:.2f} lv.")