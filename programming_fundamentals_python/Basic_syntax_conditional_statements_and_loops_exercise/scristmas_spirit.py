decorations_amount = int(input())
days_left = int(input())
ornament_set_cost = 2
ornament_set_spirit = 5
tree_skirt_cost = 5
tree_skirt_spirit = 3
tree_garland_cost = 3
tree_garland_spirit = 10
tree_lights_cost = 15
tree_lights_spirit = 17
total_money = 0
total_spirit = 0
tenth_day = False
for day in range(1, days_left+1):
    same_day = False
    tenth_day = False
    if day % 11 == 0:
        decorations_amount += 2
    if day % 2 == 0:
        total_money += ornament_set_cost * decorations_amount
        total_spirit += ornament_set_spirit
    if day % 3 == 0:
        total_money += (tree_skirt_cost * decorations_amount + tree_garland_cost * decorations_amount)
        total_spirit += (tree_skirt_spirit + tree_garland_spirit)
        same_day = True
    if day % 5 == 0:
        total_money += tree_lights_cost * decorations_amount
        total_spirit += tree_lights_spirit
        if same_day:
            total_spirit += 30
    if day % 10 == 0:
        total_money += (tree_skirt_cost + tree_garland_cost + tree_lights_cost)
        total_spirit -= 20
        tenth_day = True
if tenth_day:
    total_spirit -= 30
print(f"Total cost: {total_money}")
print(f"Total spirit: {total_spirit}")