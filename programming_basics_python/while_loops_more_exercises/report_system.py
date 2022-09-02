needed_money = int(input())
payment = 1
total_payments_amount = 0
amount_payment_cash = 0
amount_payment_card = 0
cash_payments = 0
card_payments = 0
average_cash_payments = 0
average_card_payments = 0
current_item_price = input()
while current_item_price != "End" and total_payments_amount < needed_money:
    item_price = int(current_item_price)
    if payment == 1:
        if item_price > 100:
            print("Error in transaction!")
            payment += 1
        else:
            print("Product sold!")
            amount_payment_cash += item_price
            total_payments_amount += item_price
            payment += 1
            cash_payments += 1
    elif payment == 2:
        if item_price < 10:
            print("Error in transaction!")
            payment = 1
        else:
            print("Product sold!")
            amount_payment_card += item_price
            total_payments_amount += item_price
            card_payments += 1
            payment = 1
    if total_payments_amount < needed_money:
        current_item_price = input()
if total_payments_amount < needed_money:
    print("Failed to collect required money for charity.")
elif total_payments_amount >= needed_money:
    average_cash_payments = amount_payment_cash / cash_payments
    average_card_payments = amount_payment_card / card_payments
    print(f"Average CS: {average_cash_payments:.2f}")
    print(f"Average CC: {average_card_payments:.2f}")
