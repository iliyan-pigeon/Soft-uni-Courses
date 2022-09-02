voucher_amount = int(input())
purchase_type = input()
tickets_number = 0
others_number = 0
while purchase_type != "End":
    amount = 0
    ticket_first_character = 0
    ticket_second_character = 0
    others_character = 0
    ticket_iterations = 0
    others_iterations = 0
    ticket_price = 0
    other_price = 0
    for d in enumerate(purchase_type):
        amount += 1
    if amount > 8:
        for c in purchase_type:
            ticket_iterations += 1
            if ticket_iterations == 1:
                ticket_first_character = ord(c)
            elif ticket_iterations == 2:
                ticket_second_character = ord(c)
            else:
                break
    elif amount <= 8:
        for c in purchase_type:
            others_iterations += 1
            if others_iterations == 1:
               others_character = ord(c)
            else:
                break
    ticket_price = ticket_first_character + ticket_second_character
    other_price = others_character
    if ticket_price > voucher_amount:
        break
    elif other_price > voucher_amount:
        break
    else:
        if ticket_price > 0:
            tickets_number += 1
        elif other_price > 0:
            others_number += 1
        voucher_amount -= (ticket_price + other_price)
    purchase_type = input()
print(tickets_number)
print(others_number)
