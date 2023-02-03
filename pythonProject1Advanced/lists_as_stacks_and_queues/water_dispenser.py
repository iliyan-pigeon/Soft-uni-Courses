from collections import deque

water_amount = int(input())
queue = deque()
customer = input()
while customer != "Start":
    queue.append(customer)
    customer = input()
command = input()
while command != "End":
    if "refill" in command:
        litres = int(command.split()[1])
        water_amount += litres
    else:
        litres = int(command)
        if litres > water_amount:
            print(f"{queue.popleft()} must wait")
        else:
            print(f"{queue.popleft()} got water")
            water_amount -= litres
    command = input()
print(f"{water_amount} liters left")
