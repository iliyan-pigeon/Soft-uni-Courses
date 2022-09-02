all_expelled_list = input().split(' ')
a_team = 11
b_team = 11
terminated_list = []
game_terminated = False
for card in all_expelled_list:
    if card not in terminated_list:
        terminated_list.append(card)
    elif card in terminated_list:
        continue
    player = card.split('-')
    if player[0] == 'A':
        a_team -= 1
    elif player[0] == 'B':
        b_team -= 1
    if a_team < 7 or b_team < 7:
        game_terminated = True
        break
print(f"Team A - {a_team}; Team B - {b_team}")
if game_terminated:
    print("Game was terminated")