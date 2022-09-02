budget = int(input())
season = input()
fishermans = int(input())
price = 0
price2 = 0
final_price = 0
discount1 = 0
discount2 = 0
difference = 0
if season == "Spring":
    price = 3000
    if fishermans <= 6:
        discount1 = price * 0.1
    elif fishermans <= 11:
        discount1 = price * 0.15
    elif fishermans >= 12:
        discount1 = price * 0.25
    price2 = price - discount1
    if fishermans % 2 == 0:
        discount2 = price2 * 0.05
    final_price = price2 - discount2
elif season == "Summer" or season == "Autumn":
    price = 4200
    if fishermans <= 6:
        discount1 = price * 0.1
    elif fishermans <= 11:
        discount1 = price * 0.15
    elif fishermans >= 12:
        discount1 = price * 0.25
    price2 = price - discount1
    if fishermans % 2 == 0 and season != "Autumn":
        discount2 = price2 * 0.05
    final_price = price2 - discount2
elif season == "Winter":
    price = 2600
    if fishermans <= 6:
        discount1 = price * 0.1
    elif fishermans <= 11:
        discount1 = price * 0.15
    elif fishermans >= 12:
        discount1 = price * 0.25
    price2 = price - discount1
    if fishermans % 2 == 0:
        discount2 = price2 * 0.05
    final_price = price2 - discount2
if final_price <= budget:
    difference = abs(final_price - budget)
    print(f"Yes! You have {difference:.2f} leva left.")
elif final_price > budget:
    difference = abs(final_price - budget)
    print(f"Not enough money! You need {difference:.2f} leva.")
