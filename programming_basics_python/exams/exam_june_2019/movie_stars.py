budget = float(input())
actor_name = input()
total_salaries = 0
is_enough = True
difference = 0
while actor_name != "ACTION":
    letter_counter = 0
    salary = 0
    for i in enumerate(actor_name):
        letter_counter += 1
    if letter_counter > 15:
        budget_left = budget - total_salaries
        salary = budget_left * 0.2
    elif letter_counter <= 15:
        salary = float(input())
    total_salaries += salary
    if total_salaries >= budget:
        is_enough = False
        break
    actor_name = input()
difference = abs(budget - total_salaries)
if is_enough:
    print(f"We are left with {difference:.2f} leva.")
elif not is_enough:
    print(f"We need {difference:.2f} leva for our actors.")