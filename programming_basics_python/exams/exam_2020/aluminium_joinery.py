number_joinery = int(input())
type_joinery = input()
receiving_type = input()
one_joinery_price = 0
combined_joinery_price = 0
total_joinery_price = 0
delivery_price = 0
percent_discount_one = 0
percent_discount_two = 0.04
if type_joinery == "90X130":
    one_joinery_price = 110
    if number_joinery > 60:
        percent_discount_one = 0.08
    elif number_joinery > 30:
        percent_discount_one = 0.05
elif type_joinery == "100X150":
    one_joinery_price = 140
    if number_joinery > 80:
        percent_discount_one = 0.1
    elif number_joinery > 40:
        percent_discount_one = 0.06
elif type_joinery == "130X180":
    one_joinery_price = 190
    if number_joinery > 50:
        percent_discount_one = 0.12
    elif number_joinery > 20:
        percent_discount_one = 0.07
elif type_joinery == "200X300":
    one_joinery_price = 250
    if number_joinery > 50:
        percent_discount_one = 0.14
    elif number_joinery > 25:
        percent_discount_one = 0.09
if receiving_type == "With delivery":
    delivery_price = 60
else:
    pass
combined_joinery_price = number_joinery * (one_joinery_price - (one_joinery_price * percent_discount_one))\
    + delivery_price
if number_joinery > 99:
    total_joinery_price = combined_joinery_price - (combined_joinery_price * percent_discount_two)
else:
    total_joinery_price = combined_joinery_price
if number_joinery <= 10:
    print("Invalid order")
else:
    print(f"{total_joinery_price:.2f} BGN")

