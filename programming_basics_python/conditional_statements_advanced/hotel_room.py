month = input()
nights = int(input())
price_studio = 0
total_studio = 0
price_apartment = 0
total_apartment = 0
discount_studio = 0
discount_apartment = 0
final_price_studio = 0
final_price_apartment = 0
if month == "May" or month == "October":
    price_studio = 50
    total_studio = price_studio * nights
    price_apartment = 65
    total_apartment = price_apartment * nights
    if nights > 7 and nights <= 14:
        discount_studio = total_studio * 0.05
    elif nights > 14:
        discount_studio = total_studio * 0.3
        discount_apartment = total_apartment * 0.1
elif month == "June" or month == "September":
    price_studio = 75.2
    total_studio = price_studio * nights
    price_apartment = 68.7
    total_apartment = price_apartment * nights
    if nights > 14:
        discount_studio = total_studio * 0.2
        discount_apartment = total_apartment * 0.1
elif month == "July" or month == "August":
    price_studio = 76
    total_studio = price_studio * nights
    price_apartment = 77
    total_apartment = price_apartment * nights
    if nights > 14:
        discount_apartment = total_apartment * 0.1
final_price_studio = total_studio - discount_studio
final_price_apartment = total_apartment - discount_apartment
print(f"Apartment: {final_price_apartment:.2f} lv.")
print(f"Studio: {final_price_studio:.2f} lv.")