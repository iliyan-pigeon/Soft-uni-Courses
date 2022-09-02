price_flour_per_kilo = float(input())
amount_flour_kilo = float(input())
amount_sugar_kilo = float(input())
amount_eggs_barks = int(input())
amount_yeast_packs = int(input())
price_sugar_per_kilo = price_flour_per_kilo * 0.75
price_one_eggs_bark = price_flour_per_kilo * 1.1
price_yeast_per_pack = price_sugar_per_kilo * 0.2
total_price_flour = price_flour_per_kilo * amount_flour_kilo
total_price_sugar = price_sugar_per_kilo * amount_sugar_kilo
total_price_eggs = price_one_eggs_bark * amount_eggs_barks
total_price_yeast = price_yeast_per_pack * amount_yeast_packs
total_price = total_price_sugar + total_price_yeast\
    + total_price_flour + total_price_eggs
print(f"{total_price:.2f}")
