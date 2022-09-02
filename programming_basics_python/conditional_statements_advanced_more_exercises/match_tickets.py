budget = float(input())
category = input()
number_of_people = int(input())
ticket_price = 0
transport_price = 0
money_for_tickets = 0
tickets_total_price = 0
difference = 0
if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99
if number_of_people >= 1 and number_of_people <= 4:
    transport_price = budget * 0.75
elif number_of_people <= 9:
    transport_price = budget * 0.6
elif number_of_people <= 24:
    transport_price = budget * 0.5
elif number_of_people <= 49:
    transport_price = budget * 0.4
elif number_of_people >= 50:
    transport_price = budget * 0.25
money_for_tickets = budget - transport_price
tickets_total_price = ticket_price * number_of_people
difference = abs(money_for_tickets - tickets_total_price)
if money_for_tickets >= tickets_total_price:
    print(f"Yes! You have {difference:.2f} leva left.")
elif money_for_tickets < tickets_total_price:
    print(f"Not enough money! You need {difference:.2f} leva.")
