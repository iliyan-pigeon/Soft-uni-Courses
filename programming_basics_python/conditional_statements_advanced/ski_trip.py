days = int(input())
type_of_room = input()
evaluation = input()
discount1 = 0
discount2 = 0
price_per_night = 0
price = 0
total_price = 0
final_price = 0
nights = days - 1
if type_of_room == "room for one person":
    price_per_night = 18
    price = price_per_night * nights
    if nights < 10:
        pass
    elif nights >= 10 and nights <= 15:
        pass
    elif nights > 15:
        pass
elif type_of_room == "apartment":
    price_per_night = 25
    price = price_per_night * nights
    if nights < 10:
        discount1 = price * 0.3
    elif nights >= 10 and nights <= 15:
        discount1 = price * 0.35
    elif nights > 15:
        discount1 = price * 0.5
elif type_of_room == "president apartment":
    price_per_night = 35
    price = price_per_night * nights
    if nights < 10:
        discount1 = price * 0.1
    elif nights >= 10 and nights <= 15:
        discount1 = price * 0.15
    elif nights > 15:
        discount1 = price * 0.2
total_price = price - discount1
if evaluation == "positive":
    discount2 = total_price * 0.25
    final_price = total_price + discount2
elif evaluation == "negative":
    discount2 = total_price * 0.1
    final_price = total_price - discount2
print(f"{final_price:.2f}")