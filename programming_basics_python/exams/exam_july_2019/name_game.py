player_name = input()
winner_name = ""
winner_points = 0
while player_name != "Stop":
    current_points = 0
    for i, d in enumerate(player_name):
        current_number = int(input())
        if ord(d) == current_number:
            current_points += 10
        elif ord(d) != current_number:
            current_points += 2
    if current_points >= winner_points:
        winner_points = current_points
        winner_name = player_name
    player_name = input()
print(f"The winner is {winner_name} with {winner_points} points!")