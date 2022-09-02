player_name = input()
best_player = ""
goals_scored = 0
while player_name != "END":
    number_of_goals = int(input())
    if number_of_goals > goals_scored:
        goals_scored = number_of_goals
        best_player = player_name
    if goals_scored >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if goals_scored >= 3:
    print(f"He has scored {goals_scored} goals and made a hat-trick !!!")
elif goals_scored < 3:
    print(f"He has scored {goals_scored} goals.")