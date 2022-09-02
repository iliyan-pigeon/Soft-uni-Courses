season = input()
group_type = input()
students = int(input())
nights = int(input())
sport_type = ""
price_per_night = 0
total_price = 0
final_price = 0
discount_percent = 0
discount_volume = 0
if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 9.6
        if group_type == "boys":
            sport_type = "Judo"
        elif group_type == "girls":
            sport_type = "Gymnastics"
    elif group_type == "mixed":
        price_per_night = 10
        sport_type = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 7.2
        if group_type == "boys":
            sport_type = "Tennis"
        elif group_type == "girls":
            sport_type = "Athletics"
    elif group_type == "mixed":
        price_per_night = 9.5
        sport_type = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 15
        if group_type == "boys":
            sport_type = "Football"
        elif group_type == "girls":
            sport_type = "Volleyball"
    elif group_type == "mixed":
        price_per_night = 20
        sport_type = "Swimming"
total_price = price_per_night * nights * students
if students >= 50:
    discount_percent = 0.5
    discount_volume = total_price * discount_percent
elif students >= 20:
    discount_percent = 0.15
    discount_volume = total_price * discount_percent
elif students >= 10:
    discount_percent = 0.05
    discount_volume = total_price * discount_percent
else:
    pass
final_price = total_price - discount_volume
print(f"{sport_type} {final_price:.2f} lv.")
