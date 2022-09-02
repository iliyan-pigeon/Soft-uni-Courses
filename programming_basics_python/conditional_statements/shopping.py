budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_memory_cards = int(input())
price_video_card = 250
price_video_cards = price_video_card * number_video_cards
price_processor = price_video_cards * 0.35
price_memory_card = price_video_cards * 0.1
price_processors = price_processor * number_processors
price_memory_cards = price_memory_card * number_memory_cards
total_price = price_video_cards + price_processors + price_memory_cards
if number_video_cards > number_processors:
    total_price = total_price - (total_price * 0.15)
if total_price <= budget:
    money_left = abs(budget - total_price)
    print(f'You have {money_left:.2f} leva left!')
elif total_price > budget:
    needed_money = abs(budget - total_price)
    print(f'Not enough money! You need {needed_money:.2f} leva more!')