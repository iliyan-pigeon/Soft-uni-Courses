budget = float(input())
nights_number = int(input())
price_per_night = float(input())
others_expenses_percent = int(input())
if nights_number > 7:
    price_per_night -= (price_per_night * 0.05)
other_expenses_price = budget * others_expenses_percent / 100
hotel_price = nights_number * price_per_night
total_expenses = hotel_price + other_expenses_price
difference = abs(total_expenses - budget)
if total_expenses <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
elif total_expenses > budget:
    print(f"{difference:.2f} leva needed.")