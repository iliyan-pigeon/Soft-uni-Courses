import math

guests_number = int(input())
budget = int(input())
easter_bread_price = 4
egg_price = 0.45
amount_easter_breads = 0
amount_eggs = 0
current_person = 0
difference = 0
for guest in range(1, guests_number + 1):
    amount_eggs += 2
    current_person += 1
    if current_person == 3:
        amount_easter_breads += 1
        current_person = 0
if current_person > 0:
    amount_easter_breads += 1
total_price_easter_bread = amount_easter_breads * easter_bread_price
total_price_eggs = amount_eggs * egg_price
total_price = math.ceil(total_price_easter_bread) + total_price_eggs
difference = abs(total_price - budget)
if total_price <= budget:
    print(f"Lyubo bought {amount_easter_breads} Easter bread and {amount_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
elif total_price > budget:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
