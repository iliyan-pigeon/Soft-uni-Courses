events = [str(event) for event in input().split("|")]
energy = 100
coins = 100
events_completed = True
for event in events:
    event = event.split("-")
    event_type = event[0]
    event_amount = int(event[1])
    if event_type == "rest":
        current_energy = energy
        current_energy += event_amount
        if current_energy > 100:
            current_energy = 100
        gained_energy = abs(energy - current_energy)
        print(f"You gained {gained_energy} energy.")
        energy = current_energy
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
        if coins >= event_amount:
            coins -= event_amount
            print(f"You bought {event_type}.")
        else:
            events_completed = False
            print(f"Closed! Cannot afford {event_type}.")
            break
if events_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")