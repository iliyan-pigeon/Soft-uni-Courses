money_needed = float(input())
money_in_hand = float(input())
days_consecutive_spending = 0
days_gone_by = 0
money_are_saved = True
while money_needed > money_in_hand:
    if days_consecutive_spending == 5:
        money_are_saved = False
        break
    spend_or_save = input()
    amount_for_the_day = float(input())
    if spend_or_save == "save":
        days_gone_by += 1
        days_consecutive_spending = 0
        money_in_hand += amount_for_the_day
    elif spend_or_save == "spend":
        days_gone_by += 1
        days_consecutive_spending += 1
        if amount_for_the_day > money_in_hand:
            money_in_hand = 0
        else:
            money_in_hand -= amount_for_the_day
if money_are_saved:
    print(f"You saved the money for {days_gone_by} days.")
elif money_are_saved == False:
    print("You can't save the money.")
    print(days_gone_by)
