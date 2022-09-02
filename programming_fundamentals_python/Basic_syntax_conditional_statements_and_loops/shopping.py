budget = int(input())
command = input()
all_bought = True
combined_prices = 0
while command != "End":
    if int(command) + combined_prices > budget:
        all_bought = False
        break
    combined_prices += int(command)
    command = input()
if all_bought:
    print("You bought everything needed.")
elif not all_bought:
    print("You went in overdraft!")
