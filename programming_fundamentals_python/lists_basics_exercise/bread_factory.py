events = input().split("|")
energy = 100
coins = 100
current_energy = energy
day_completed = True
for event in events:
    event = event.split("-")
    event_type = event[0]
    event_amount = int(event[1])
    if event_type == "rest":
        energy += event_amount
        if energy > 100:
            energy = 100
        gained_energy = abs(energy - current_energy)
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_type == "order":
        if energy >= 30:
            coins += event_amount
            energy -= 30
            print(f"You earned {event_amount} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        ingredient = event_type
        price = event_amount
        if coins >= price:
            coins -= price
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            day_completed = False
            break
    current_energy = energy
if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
