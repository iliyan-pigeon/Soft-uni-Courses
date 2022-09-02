film_name = input()
hall_type = input()
tickets_number = int(input())
price_per_ticket = 0
total_income = 0
if film_name == "A Star Is Born":
    if hall_type == "normal":
        price_per_ticket = 7.5
    elif hall_type == "luxury":
        price_per_ticket = 10.5
    elif hall_type == "ultra luxury":
        price_per_ticket = 13.5
elif film_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        price_per_ticket = 7.35
    elif hall_type == "luxury":
        price_per_ticket = 9.45
    elif hall_type == "ultra luxury":
        price_per_ticket = 12.75
elif film_name == "Green Book":
    if hall_type == "normal":
        price_per_ticket = 8.15
    elif hall_type == "luxury":
        price_per_ticket = 10.25
    elif hall_type == "ultra luxury":
        price_per_ticket = 13.25
elif film_name == "The Favourite":
    if hall_type == "normal":
        price_per_ticket = 8.75
    elif hall_type == "luxury":
        price_per_ticket = 11.55
    elif hall_type == "ultra luxury":
        price_per_ticket = 13.95
total_income = price_per_ticket * tickets_number
print(f"{film_name} -> {total_income:.2f} lv.")