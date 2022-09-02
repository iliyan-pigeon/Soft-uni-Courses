destination = input()
range_of_days = input()
number_of_nights = int(input())
total_price = 0
price_per_night = 0
if destination == "France":
    if range_of_days == "21-23":
        price_per_night = 30
    elif range_of_days == "24-27":
        price_per_night = 35
    elif range_of_days == "28-31":
        price_per_night = 40
elif destination == "Italy":
    if range_of_days == "21-23":
        price_per_night = 28
    elif range_of_days == "24-27":
        price_per_night = 32
    elif range_of_days == "28-31":
        price_per_night = 39
elif destination == "Germany":
    if range_of_days == "21-23":
        price_per_night = 32
    elif range_of_days == "24-27":
        price_per_night = 37
    elif range_of_days == "28-31":
        price_per_night = 43
total_price = price_per_night * number_of_nights
print(f"Easter trip to {destination} : {total_price:.2f} leva.")
