rent_price = float(input())
cake_price = rent_price * 0.2
drinks_price = cake_price * 0.55
animator = rent_price / 3
budget_needed = rent_price + cake_price +\
    drinks_price + animator
print(f"{budget_needed:.1f}")