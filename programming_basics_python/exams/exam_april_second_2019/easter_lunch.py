number_easter_breads = int(input())
eggs_barks_number = int(input())
kilogram_cookies = int(input())
easter_bread_price = 3.2
egg_bark_price = 4.35
kilogram_cookies_price = 5.4
eggs_in_one_bark = 12
eggs_paint_per_egg_price = 0.15
easter_bread_total_price = easter_bread_price * number_easter_breads
eggs_total_price = egg_bark_price * eggs_barks_number
cookies_total_price = kilogram_cookies_price * kilogram_cookies
eggs_paint_total = (eggs_barks_number * eggs_in_one_bark) * eggs_paint_per_egg_price
total_value = easter_bread_total_price + eggs_total_price\
+ cookies_total_price + eggs_paint_total
print(f"{total_value:.2f}")

