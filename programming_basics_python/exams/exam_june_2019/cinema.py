capacity = int(input())
number_current_people = input()
number_people = 0
ticket_price = 5
discount = 5
income = 0
current_income = 0
difference = 0
is_full = False
while number_current_people != "Movie time!":
    amount_current_people = int(number_current_people)
    number_people += amount_current_people
    if number_people > capacity:
        is_full = True
        break
    if amount_current_people % 3 == 0:
        current_income = amount_current_people * ticket_price - discount
    elif amount_current_people % 3 != 0:
        current_income = amount_current_people * ticket_price
    income += current_income
    number_current_people = input()
difference = abs(number_people - capacity)
if not is_full:
    print(f"There are {difference} seats left in the cinema.")
if is_full:
    print("The cinema is full.")
print(f"Cinema income - {income} lv.")