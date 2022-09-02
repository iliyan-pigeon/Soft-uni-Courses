city_name = input()
package_type = input()
vip_discount = input()
days_number = int(input())
total_price = 0
price_per_day = 0
discount = 0
correct_input = True
correct_days = True
if city_name == "Bansko" or city_name == "Borovets":
    if package_type == "noEquipment":
        price_per_day = 80
        discount = 0.05
    elif package_type == "withEquipment":
        price_per_day = 100
        discount = 0.1
    else:
        correct_input = False
elif city_name == "Varna" or city_name == "Burgas":
    if package_type == "noBreakfast":
        price_per_day = 100
        discount = 0.07
    elif package_type == "withBreakfast":
        price_per_day = 130
        discount = 0.12
    else:
        correct_input = False
else:
    correct_input = False
if vip_discount == "yes":
    price_per_day -= (price_per_day * discount)
total_price = price_per_day * days_number
if days_number < 1:
    correct_days = False
elif days_number > 7:
    total_price -= price_per_day
if correct_input and correct_days:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif not correct_input:
    print("Invalid input!")
elif not correct_days:
    print("Days must be positive number!")
