items = [str(i) for i in input().split("|")]
budget = int(input())
total_price = 0
money_needed = 150
budget_left = budget
profit = 0
new_prices = []
new_prices_string = []
for item in items:
    item = item.split("->")
    item_type = item[0]
    item_price = float(item[1])
    should_buy = False
    if item_price <= budget_left:
        if item_type == "Clothes" and item_price <= 50:
            should_buy = True
        elif item_type == "Shoes" and item_price <= 35:
            should_buy = True
        elif item_type == "Accessories" and item_price <= 20.50:
            should_buy = True
    if should_buy:
        budget_left -= item_price
        item_new_price = item_price + (item_price * 0.4)
        new_prices.append(item_new_price)
        profit += item_price * 0.4
        total_price = profit + budget
for price in new_prices:
    price = f"{price:.2f}"
    new_prices_string.append(str(price))
print(" ".join(new_prices_string))
print(f"Profit: {profit:.2f}")
if total_price >= money_needed:
    print("Hello, France!")
else:
    print("Not enough money.")