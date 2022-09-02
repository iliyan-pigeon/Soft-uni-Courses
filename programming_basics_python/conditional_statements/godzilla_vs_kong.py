film_budget = float(input())
film_statists = int(input())
price_per_outfit = float(input())
decor = film_budget * 10 / 100
outfit_price_combined = film_statists * price_per_outfit
if film_statists > 150:
    outfit_price_combined *= 0.9
price_all_combined = outfit_price_combined + decor
if price_all_combined > film_budget:
    money_needed = price_all_combined - film_budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
elif price_all_combined <= film_budget:
    money_left = film_budget - price_all_combined
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')