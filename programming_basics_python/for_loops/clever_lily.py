age_of_lily = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())
difference = 0
money_per_year = 0
total_money = 0
amount_of_toys = 0
toy_total_price = 0
final_money_amount = 0
stolen_from_her_brother = 0
for age in range(1, age_of_lily +1):
    if age % 2 == 0:
        money_per_year += 10
        total_money += money_per_year
        stolen_from_her_brother += 1
    else:
        amount_of_toys += 1
toy_total_price = amount_of_toys * price_per_toy
final_money_amount = (total_money - stolen_from_her_brother) + toy_total_price
difference = abs(final_money_amount - washing_machine_price)
if final_money_amount >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
elif final_money_amount < washing_machine_price:
    print(f"No! {difference:.2f}")



