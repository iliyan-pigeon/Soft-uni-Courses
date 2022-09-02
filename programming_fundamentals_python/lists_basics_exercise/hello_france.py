items_collection = input().split("|")
budget = float(input())
the_budget = budget
ticket_price = 150
profit = 0
increase = 0.4
new_prices_list = []
for item in items_collection:
    the_item = item.split("->")
    item_type = the_item[0]
    item_price = float(the_item[1])
    new_price = 0
    can_bye = True
    bought = False
    if the_budget < item_price:
        can_bye = False
    if item_type == "Clothes" and item_price <= 50 and can_bye:
        bought = True
    elif item_type == "Shoes" and item_price <= 35 and can_bye:
        bought = True
    elif item_type == "Accessories" and item_price <= 20.50 and can_bye:
        bought = True
    if bought:
        the_budget -= item_price
        mark_up = item_price * increase
        new_price = item_price + mark_up
        profit += mark_up
        new_prices_list.append(f"{new_price:.2f}")
new_prices = " ".join(new_prices_list)
print(new_prices)
print(f"Profit: {profit:.2f}")
if budget + profit >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
