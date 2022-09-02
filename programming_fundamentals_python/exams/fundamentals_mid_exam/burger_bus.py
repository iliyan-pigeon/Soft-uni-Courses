cities_number = int(input())
total_profit = 0
for city in range(1, cities_number+1):
    city_name = input()
    current_income = float(input())
    current_expenses = float(input())
    if city % 3 == 0:
        if city % 5 != 0:
            current_expenses += (current_expenses * 0.5)
    if city % 5 == 0:
        current_income -= (current_income * 0.1)
    current_profit = current_income - current_expenses
    total_profit += current_profit
    print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")