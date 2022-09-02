fuel_type = input()
fuel_amount = float(input())
if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")
else:
    if fuel_amount >= 25:
      print(f"You have enough {str.lower(fuel_type)}.")
    elif fuel_amount < 25:
      print(f"Fill your tank with {str.lower(fuel_type)}!")