budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_liter_milk = price_kg_flour + (price_kg_flour * 0.25)
money_spend = 0
loaves_number = 0
eggs_number = 0
should_beak = True
counter = 0
while should_beak:
    current_price = price_kg_flour + price_pack_eggs + (price_liter_milk * 0.25)
    if money_spend + current_price > budget:
        should_beak = False
        continue
    money_spend += current_price
    loaves_number += 1
    eggs_number += 3
    counter += 1
    if counter == 3:
        counter = 0
        eggs_number -= (loaves_number - 2)
difference = abs(budget - money_spend)
print(f"You made {loaves_number} loaves of Easter bread! Now you have {eggs_number} eggs and {difference:.2f}BGN left.")