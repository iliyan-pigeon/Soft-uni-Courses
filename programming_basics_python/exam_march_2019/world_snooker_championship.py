championship_stage = input()
type_of_ticket = input()
number_of_tickets = int(input())
picture_with_trophy = input()
ticket_price = 0
total_price = 0
trophy_picture_price = 40
final_price = 0
if championship_stage == "Quarter final":
    if type_of_ticket == "Standard":
        ticket_price = 55.50
    elif type_of_ticket == "Premium":
        ticket_price = 105.20
    elif type_of_ticket == "VIP":
        ticket_price = 118.90
elif championship_stage == "Semi final":
    if type_of_ticket == "Standard":
        ticket_price = 75.88
    elif type_of_ticket == "Premium":
        ticket_price = 125.22
    elif type_of_ticket == "VIP":
        ticket_price = 300.40
elif championship_stage == "Final":
    if type_of_ticket == "Standard":
        ticket_price = 110.10
    elif type_of_ticket == "Premium":
        ticket_price = 160.66
    elif type_of_ticket == "VIP":
        ticket_price = 400
total_price = ticket_price * number_of_tickets
if total_price > 4000:
    final_price = total_price - (total_price * 0.25)
elif total_price > 2500:
    if picture_with_trophy == "Y":
        final_price = (total_price - (total_price * 0.1)) + (trophy_picture_price * number_of_tickets)
    elif picture_with_trophy == "N":
        final_price = total_price - (total_price * 0.1)
else:
    if picture_with_trophy == "Y":
        final_price = total_price + (trophy_picture_price * number_of_tickets)
    elif picture_with_trophy == "N":
        final_price = total_price
print(f"{final_price:.2f}")


