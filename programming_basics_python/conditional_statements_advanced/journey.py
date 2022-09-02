budget = float(input())
season = input()
price = 0
destination = ""
type_of_vacation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        type_of_vacation = "Camp"
    elif season == "winter":
        price = budget * 0.70
        type_of_vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        type_of_vacation = "Camp"
    elif season == "winter":
        price = budget * 0.80
        type_of_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.90
    type_of_vacation = "Hotel"
print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {price:.2f}")