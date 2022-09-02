data = input().split(": ")
products = {}
for i in range(0, len(data), 2):
    products[data[i]] = int(data[i+1])
command = input()
while command != "statistics":
    command = command.split(": ")
    product = command[0]
    amount = int(command[1])
    if product in products:
        products[product] += amount
    elif product not in products:
        products[product] = int(amount)
    command = input()
print("Products in stock:")
for item in products:
    result = f"- {item}: {products[item]}"
    print(result)
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

