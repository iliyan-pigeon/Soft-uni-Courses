budget = float(input())
series_number = int(input())
difference = 0
total_price = 0
for series in range(series_number):
    series_name = input()
    series_price = float(input())
    discount = 0
    if series_name == "Thrones":
        discount = series_price * 0.5
        series_price -= discount
    elif series_name == "Lucifer":
        discount = series_price * 0.4
        series_price -= discount
    elif series_name == "Protector":
        discount = series_price * 0.3
        series_price -= discount
    elif series_name == "TotalDrama":
        discount = series_price * 0.2
        series_price -= discount
    elif series_name == "Area":
        discount = series_price * 0.1
        series_price -= discount
    total_price += series_price
difference = abs(total_price - budget)
if total_price <= budget:
    print(f"You bought all the series and left with {difference:.2f} lv.")
elif total_price > budget:
    print(f"You need {difference:.2f} lv. more to buy the series!")