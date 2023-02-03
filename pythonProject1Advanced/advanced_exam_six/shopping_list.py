def shopping_list(money_amount, **kwargs):
    result = ''
    if money_amount < 100:
        return "You do not have enough budget."

    bought_products_type = 0

    for product, value in kwargs.items():
        if bought_products_type == 5:
            break

        product_type = product
        product_price = float(value[0])
        products_amount = int(value[1])
        combined_price = product_price * products_amount
        if combined_price <= money_amount:
            money_amount -= combined_price
            bought_products_type += 1
            result +=  f"You bought {product_type} for {combined_price:.2f} leva.\n"
    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))