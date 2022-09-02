players_data = {}
total_skill_data = {}
command = input()
while command != "Season end":
    if " -> " in command:
        command = command.split(" -> ")
        player = command[0]
        position = command[1]
        skill = int(command[2])
        if player not in players_data:
            players_data[player] = {}
            total_skill_data[player] = 0
        if position not in players_data[player]:
            players_data[player][position] = skill
            total_skill_data[player] += skill
        if players_data[player][position] < skill:
            total_skill_data[player] += abs(players_data[player][position] - skill)
            players_data[player][position] = skill
    elif " vs " in command:
        command = command.split(" vs ")
        first_player = command[0]
        second_player = command[1]
        if first_player in players_data and second_player in players_data:
            match_position = [p for p in players_data[first_player] if p in players_data[second_player]]
            if match_position:
                if total_skill_data[first_player] > total_skill_data[second_player]:
                    players_data.pop(second_player)
                    total_skill_data.pop(second_player)
                elif total_skill_data[first_player] < total_skill_data[second_player]:
                    players_data.pop(first_player)
                    total_skill_data.pop(first_player)
    command = input()
ordered_skill_data = sorted(total_skill_data.items(), key=lambda x: (-x[1], x[0]))
for player in ordered_skill_data:
    print(f"{player[0]}: {player[1]} skill")
    ordered_player_skills = sorted(players_data[player[0]].items(), key=lambda x: (-x[1], x[0]))
    for skill in ordered_player_skills:
        print(f"- {skill[0]} <::> {skill[1]}")
