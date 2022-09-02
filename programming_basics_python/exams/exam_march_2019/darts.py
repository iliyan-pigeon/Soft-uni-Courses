player_name = input()
start_points = 301
successful_shots = 0
unsuccessful_shots = 0
is_successful = True
while start_points != 0:
    function = input()
    if function == "Retire":
        is_successful = False
        break
    current_points = int(input())
    if function == "Single":
        current_points = current_points
    elif function == "Double":
        current_points = current_points * 2
    elif function == "Triple":
        current_points = current_points * 3
    if current_points > start_points:
        unsuccessful_shots += 1
    elif current_points <= start_points:
        successful_shots += 1
        start_points -= current_points
if is_successful:
    print(f"{player_name} won the leg with {successful_shots} shots.")
elif not is_successful:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")

