products_data = {}
command = input()
while command != "buy":
    product = command.split()
    product_type = product[0]
    product_price = float(product[1])
    product_amount = int(product[2])
    if product_type not in products_data:
        products_data[product_type] = [product_price, product_amount]
    elif product_type in products_data:
        products_data[product_type][0] = product_price
        products_data[product_type][1] += product_amount
    command = input()
for product, value in products_data.items():
    total_value = value[0] * value[1]
    print(f"{product} -> {total_value:.2f}")
