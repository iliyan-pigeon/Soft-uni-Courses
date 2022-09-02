destination = input()
budget_needed = float(input())
while destination != "End":
    saved_money = 0
    while budget_needed > saved_money:
        current_saved_money = float(input())
        saved_money += current_saved_money
    if budget_needed <= saved_money:
        print(f"Going to {destination}!")
    destination = input()
    if destination == "End":
        break
    budget_needed = float(input())

