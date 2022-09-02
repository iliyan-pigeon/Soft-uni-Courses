money_in_hand = float(input())
gender = input()
age = int(input())
sport = input()
monthly_price = 0
total_price = 0
difference = 0
if gender == "m":
    if sport == "Gym":
        monthly_price = 42
    elif sport == "Boxing":
        monthly_price = 41
    elif sport == "Yoga":
        monthly_price = 45
    elif sport == "Zumba":
        monthly_price = 34
    elif sport == "Dances":
        monthly_price = 51
    elif sport == "Pilates":
        monthly_price = 39
elif gender == "f":
    if sport == "Gym":
        monthly_price = 35
    elif sport == "Boxing":
        monthly_price = 37
    elif sport == "Yoga":
        monthly_price = 42
    elif sport == "Zumba":
        monthly_price = 31
    elif sport == "Dances":
        monthly_price = 53
    elif sport == "Pilates":
        monthly_price = 37
if age <= 19:
    monthly_price = monthly_price * 0.8
if monthly_price <= money_in_hand:
    print(f"You purchased a 1 month pass for {sport}.")
elif monthly_price > money_in_hand:
    difference = abs(money_in_hand - monthly_price)
    print(f"You don't have enough money! You need ${difference:.2f} more.")