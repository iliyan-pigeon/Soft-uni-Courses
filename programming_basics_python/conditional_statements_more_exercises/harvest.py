import math
vineyard_sq_m = int(input())
grapes_kg_per_sq_m = float(input())
wine_litres_needed = int(input())
number_workers = int(input())
difference = 0
litres_wine = 0
litres_per_worker = 0
total_grapes = vineyard_sq_m * grapes_kg_per_sq_m
percent_for_wine = 0.4
grapes_for_wine = total_grapes * 0.4
litres_wine = grapes_for_wine / 2.5
difference = abs(litres_wine - wine_litres_needed)
if litres_wine < wine_litres_needed:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
elif litres_wine >= wine_litres_needed:
    litres_per_worker = difference / number_workers
    print(f"Good harvest this year! Total wine: {math.floor(litres_wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(litres_per_worker)} liters per person.")



