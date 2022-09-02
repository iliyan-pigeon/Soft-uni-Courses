drink_type = input()
sugar_amount = input()
drinks_number = int(input())
drink_price = 0
total_price = 0
final_price = 0
discount_one = 0.35
discount_two = 0.25
discount_three = 0.2
if drink_type == "Espresso":
    if sugar_amount == "Without":
        drink_price = 0.9 - (0.9 * discount_one)
    elif sugar_amount == "Normal":
        drink_price = 1
    elif sugar_amount == "Extra":
        drink_price = 1.2
    if drinks_number >= 5:
        drink_price -= (drink_price * discount_two)
elif drink_type == "Cappuccino":
    if sugar_amount == "Without":
        drink_price = 1 - (1 * discount_one)
    elif sugar_amount == "Normal":
        drink_price = 1.2
    elif sugar_amount == "Extra":
        drink_price = 1.6
elif drink_type == "Tea":
    if sugar_amount == "Without":
        drink_price = 0.5 - (0.5 * discount_one)
    elif sugar_amount == "Normal":
        drink_price = 0.6
    elif sugar_amount == "Extra":
        drink_price = 0.7
total_price = drink_price * drinks_number
if total_price > 15:
    final_price = total_price - (total_price * discount_three)
else:
    final_price = total_price
print(f"You bought {drinks_number} cups of {drink_type} for {final_price:.2f} lv.")