waiting_people = int(input())
lift_wagons_state = [int(wagon) for wagon in input().split()]
no_queue = False
for wagon in range(len(lift_wagons_state)):
    while lift_wagons_state[wagon] != 4:
        if waiting_people <= 0:
            no_queue = True
            break
        lift_wagons_state[wagon] += 1
        waiting_people -= 1
    if no_queue:
        break
if 3 in lift_wagons_state or 2 in lift_wagons_state or 1 in lift_wagons_state or 0 in lift_wagons_state and no_queue:
    print("The lift has empty spots!")
    lift_wagons_str = list(map(str, lift_wagons_state))
    print(f"{' '.join(lift_wagons_str)}")
elif 3 not in lift_wagons_state or 2 not in lift_wagons_state or 1 not in lift_wagons_state or 0 not in lift_wagons_state and not no_queue:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    lift_wagons_str = list(map(str, lift_wagons_state))
    print(f"{' '.join(lift_wagons_str)}")
elif 3 not in lift_wagons_state or 2 not in lift_wagons_state or 1 not in lift_wagons_state or 0 not in lift_wagons_state and no_queue:
    lift_wagons_str = list(map(str, lift_wagons_state))
    print(f"{' '.join(lift_wagons_str)}")

