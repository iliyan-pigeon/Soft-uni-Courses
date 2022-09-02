sent_off_players = input().split(" ")
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
terminated_game = False
for sent_off in sent_off_players:
    player_info = sent_off.split('-')
    team = player_info[0]
    player = int(player_info[1])
    if team == "A":
        if player in team_a:
            team_a.remove(player)
    elif team == "B":
        if player in team_b:
            team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        terminated_game = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated_game:
    print("Game was terminated")