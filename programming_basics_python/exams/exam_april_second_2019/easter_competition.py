easter_breads_number = int(input())
winner = ""
winners_points = 0
for bread in range(easter_breads_number):
    baker_name = input()
    current_evaluation = input()
    total_points = 0
    while current_evaluation != "Stop":
        current_points = int(current_evaluation)
        total_points += current_points
        current_evaluation = input()
    print(f"{baker_name} has {total_points} points.")
    if total_points > winners_points:
        winners_points = total_points
        winner = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{winner} won competition with {winners_points} points!")

