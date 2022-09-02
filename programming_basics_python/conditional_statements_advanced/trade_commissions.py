city = input()
sales_volume = float(input())
is_valid = True
commission = 0
if city == "Sofia":
    if sales_volume >= 0 and sales_volume <= 500:
        commission = 0.05
    elif sales_volume > 500 and sales_volume <= 1000:
        commission = 0.07
    elif sales_volume > 1000 and sales_volume <= 10000:
        commission = 0.08
    elif sales_volume > 10000:
        commission = 0.12
    else:
        is_valid = False
elif city == "Varna":
    if sales_volume >= 0 and sales_volume <= 500:
        commission = 0.045
    elif sales_volume > 500 and sales_volume <= 1000:
        commission = 0.075
    elif sales_volume > 1000 and sales_volume <= 10000:
        commission = 0.1
    elif sales_volume > 10000:
        commission = 0.13
    else:
        is_valid = False
elif city == "Plovdiv":
    if sales_volume >= 0 and sales_volume <= 500:
        commission = 0.055
    elif sales_volume > 500 and sales_volume <= 1000:
        commission = 0.08
    elif sales_volume > 1000 and sales_volume <= 10000:
        commission = 0.12
    elif sales_volume > 10000:
        commission = 0.145
    else:
        is_valid = False
else:
    is_valid = False
if is_valid:
    commission_price = sales_volume * commission
    print(f"{commission_price:.2f}")
else:
    print("error")

