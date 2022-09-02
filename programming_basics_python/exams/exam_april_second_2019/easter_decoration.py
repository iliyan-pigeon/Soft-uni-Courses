clients_number = int(input())
basket_price = 1.5
wreath_price = 3.8
chocolate_bunny_price = 7
average_bill_amount = 0
combined_amount_clients = 0
for client in range(clients_number):
    chosen_item = input()
    items_number = 0
    final_price = 0
    while chosen_item != "Finish":
        items_number += 1
        if chosen_item == "basket":
            final_price += basket_price
        elif chosen_item == "wreath":
            final_price += wreath_price
        elif chosen_item == "chocolate bunny":
            final_price += chocolate_bunny_price
        chosen_item = input()
    if items_number % 2 == 0:
        final_price -= (final_price * 0.2)
    combined_amount_clients += final_price
    print(f"You purchased {items_number} items for {final_price:.2f} leva.")
average_bill_amount = combined_amount_clients / clients_number
print(f"Average bill per client is: {average_bill_amount:.2f} leva.")
