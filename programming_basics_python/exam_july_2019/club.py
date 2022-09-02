needed_target = float(input())
cocktail_name = input()
total_income = 0
difference = 0
discount = 0.25
reached_target = False
while cocktail_name != "Party!":
    cocktails_number = int(input())
    cocktail_price = 0
    current_price = 0
    for c in range(len(cocktail_name)):
        cocktail_price += 1
    current_price = cocktail_price * cocktails_number
    if current_price % 2 != 0:
        current_price -= (current_price * discount)
    total_income += current_price
    if total_income >= needed_target:
        reached_target = True
        break
    cocktail_name = input()
if reached_target:
    print("Target acquired.")
elif not reached_target:
    difference = abs(total_income - needed_target)
    print(f"We need {difference:.2f} leva more.")
print(f"Club income - {total_income:.2f} leva.")
