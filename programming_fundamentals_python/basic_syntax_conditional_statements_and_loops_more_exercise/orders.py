orders_number = int(input())
total_price = 0
for order in range(orders_number):
    price_per_capsule = float(input())
    days = int(input())
    number_capsules = int(input())
    current_price = price_per_capsule * number_capsules * days
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")
print(f"Total: ${total_price:.2f}")