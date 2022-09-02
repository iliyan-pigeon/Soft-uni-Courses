combined_price = 0
tax_price = 0
total_price = 0
valid_order = True
is_special = False
while True:
    command = input()
    if command == "special":
        if combined_price <= 0:
            valid_order = False
        is_special = True
        break
    elif command == "regular":
        if combined_price <= 0:
            valid_order = False
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        combined_price += price
        tax_price += (price * 0.2)
if valid_order:
    if is_special:
        discount = (combined_price + tax_price) * 0.1
        total_price = (combined_price + tax_price) - discount
    elif not is_special:
        total_price = combined_price + tax_price
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {combined_price:.2f}$")
    print(f"Taxes: {tax_price:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
elif not valid_order:
    print("Invalid order!")
