budget = float(input())
destination = input()
season = input()
days_number = int(input())
day_price = 0
difference = 0
increase = 0
discount = 0
total_price = 0
final_price = 0
if destination == "Dubai":
    if season == "Winter":
        day_price = 45000
    elif season == "Summer":
        day_price = 40000
elif destination == "Sofia":
    if season == "Winter":
        day_price = 17000
    elif season == "Summer":
        day_price = 12500
elif destination == "London":
    if season == "Winter":
        day_price = 24000
    elif season == "Summer":
        day_price = 20250
total_price = day_price * days_number
if destination == "Dubai":
    discount = total_price * 0.3
    final_price = total_price - discount
elif destination == "Sofia":
    increase = total_price * 0.25
    final_price = total_price + increase
else:
    final_price = total_price
difference = abs(final_price - budget)
if final_price <= budget:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
elif final_price > budget:
    print(f"The director needs {difference:.2f} leva more!")