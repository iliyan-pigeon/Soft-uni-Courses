quantity = int(input())
days = int(input())
ornament_set = 2
tree_skirts = 5
tree_garlands = 3
tree_lights = 15
total_price = 0
total_spirit = 0
for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2
    should_increase = False
    if day % 2 == 0:
        total_price += ornament_set * quantity
        total_spirit += 5
    if day % 3 == 0:
        total_price += ((tree_skirts + tree_garlands) * quantity)
        total_spirit += 13
        should_increase = True
    if day % 5 == 0:
        total_price += tree_lights * quantity
        total_spirit += 17
        if should_increase:
            total_spirit += 30
    if day % 10 == 0:
        total_price += (tree_skirts + tree_garlands + tree_lights)
        total_spirit -= 20
        if day == days:
            total_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")