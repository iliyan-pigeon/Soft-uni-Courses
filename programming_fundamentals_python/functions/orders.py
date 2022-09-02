def products_calculator(product: str, amount: int):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return f"{price * amount:.2f}"


product_type = input()
number_of_products = int(input())
result = products_calculator(product_type, number_of_products)
print(result)