chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery_price = 2.50
count_chicken = int(input())
count_fish = int(input())
count_vegetarian = int(input())
menus_total_price = chicken_menu * count_chicken \
    + fish_menu * count_fish + vegetarian_menu * count_vegetarian
desert_price = menus_total_price * float(0.2)
order_total_price = menus_total_price + desert_price + delivery_price
print(order_total_price)