film_budget = float(input())
number_of_statists = int(input())
single_outfit_price = float(input())
decor = film_budget * 0.1
if number_of_statists > 150:
    single_outfit_price = single_outfit_price * 0.9
elif number_of_statists <= 150:
    single_outfit_price = single_outfit_price
combined_outfit_price = number_of_statists * single_outfit_price
total_price = combined_outfit_price + decor
difference = abs(film_budget - total_price)
if total_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
elif total_price <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")