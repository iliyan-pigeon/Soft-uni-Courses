import math

racket_price = float(input())
rackets_number = int(input())
sneakers_number = int(input())
pair_sneakers_price = racket_price / 6
total_rackets_price = racket_price * rackets_number
total_sneakers_price = pair_sneakers_price * sneakers_number
combined_rackets_sneakers_price = total_sneakers_price + total_rackets_price
other_equipment_price = combined_rackets_sneakers_price * 0.2
total_price = combined_rackets_sneakers_price + other_equipment_price
price_for_sponsors = (total_price / 8) * 7
price_for_player = total_price / 8
print(f"Price to be paid by Djokovic {math.floor(price_for_player)}")
print(f"Price to be paid by sponsors {math.ceil(price_for_sponsors)}")