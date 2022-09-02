fruit = input()
size = input()
sets_number = int(input())
price_per_set = 0
discount_one =  0.15
discount_two = 0.5
discount_amount = 0
total_price = 0
if fruit == "Watermelon":
    if size == "small":
        price_per_set = 56 * 2
    elif size == "big":
        price_per_set = 28.7 * 5
elif fruit == "Mango":
    if size == "small":
        price_per_set = 36.66 * 2
    elif size == "big":
        price_per_set = 19.6 * 5
elif fruit == "Pineapple":
    if size == "small":
        price_per_set = 42.10 * 2
    elif size == "big":
        price_per_set = 24.8 * 5
elif fruit == "Raspberry":
    if size == "small":
        price_per_set = 20 * 2
    elif size == "big":
        price_per_set = 15.2 * 5
total_price = price_per_set * sets_number
if 400 <= total_price <= 1000:
    discount_amount = total_price * discount_one
    total_price -= discount_amount
elif total_price > 1000:
    discount_amount = total_price * discount_two
    total_price -= discount_amount
else:
    total_price = total_price
print(f"{total_price:.2f} lv.")