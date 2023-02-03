def shopping_cart(*kwargs):
    result = ""
    soup_products_limit = 3
    pizza_products_limit = 4
    dessert_products_limit = 2
    products_dict = {"Soup": [], "Pizza": [], "Dessert": []}

    for kwarg in kwargs:
        if kwarg == "Stop":
            break
        meal = kwarg[0]
        product = kwarg[1]
        if meal == "Soup":
            if len(products_dict[meal]) < soup_products_limit and product not in products_dict[meal]:
                products_dict[meal].append(product)
        elif meal == "Pizza":
            if len(products_dict[meal]) < pizza_products_limit and product not in products_dict[meal]:
                products_dict[meal].append(product)
        elif meal == "Dessert":
            if len(products_dict[meal]) < dessert_products_limit and product not in products_dict[meal]:
                products_dict[meal].append(product)

    products_dict = sorted(products_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    if not products_dict[0][1] and not products_dict[1][1] and not products_dict[2][1]:
        return "No products in the cart!"
    for meal in products_dict:
        the_meal = meal[0]
        products = sorted(meal[1])
        result += f"{the_meal}:\n"
        for product in products:
            result += f" - {product}\n"
    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))