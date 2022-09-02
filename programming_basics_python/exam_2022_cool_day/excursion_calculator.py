number_of_people = int(input())
season = input()
price_per_person = 0
total_price = 0
final_price = 0
summer_discount = 0.15
winter_increase = 0.08
if number_of_people <= 5:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.5
    elif season == "autumn":
        price_per_person = 60
    elif season == "winter":
        price_per_person = 86
elif number_of_people > 5:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.5
    elif season == "winter":
        price_per_person = 85
total_price = price_per_person * number_of_people
if season == "summer":
    final_price = total_price - (total_price * summer_discount)
elif season == "winter":
    final_price = total_price + (total_price * winter_increase)
else:
    final_price = total_price
print(f"{final_price:.2f} leva.")
