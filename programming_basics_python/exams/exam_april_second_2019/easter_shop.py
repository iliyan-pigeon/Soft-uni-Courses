amount_eggs = int(input())
sold_eggs = 0
eggs_left = amount_eggs
command = input()
are_enough = True
while command != "Close":
    current_amount_eggs = int(input())
    if command == "Buy":
        if current_amount_eggs > eggs_left:
            are_enough = False
            break
        eggs_left -= current_amount_eggs
        sold_eggs += current_amount_eggs
    elif command == "Fill":
        eggs_left += current_amount_eggs
    command = input()
if are_enough:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
elif not are_enough:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_left}.")