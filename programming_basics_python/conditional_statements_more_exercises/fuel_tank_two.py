type_of_fuel = input()
amount_of_fuel = float(input())
club_card = input()
discount_one = 0
discount_two = 0
total_price = 0
final_price = 0
price_gasoline = 2.22
price_diesel = 2.33
price_gas =0.93
if type_of_fuel == "Gasoline":
    if club_card == "Yes":
        discount_one = 0.18
    elif club_card == "No":
        pass
    total_price = amount_of_fuel * (price_gasoline - discount_one)
elif type_of_fuel == "Diesel":
    if club_card == "Yes":
        discount_one = 0.12
    elif club_card == "No":
        pass
    total_price = amount_of_fuel * (price_diesel - discount_one)
elif type_of_fuel == "Gas":
    if club_card == "Yes":
        discount_one = 0.08
    elif club_card == "No":
        pass
    total_price = amount_of_fuel * (price_gas - discount_one)
if amount_of_fuel >= 20 and amount_of_fuel <= 25:
    discount_two = 0.08
elif amount_of_fuel > 25:
    discount_two = 0.1
else:
    pass
discount_two_amount = total_price * discount_two
final_price = total_price - discount_two_amount
print(f"{final_price:.2f} lv.")