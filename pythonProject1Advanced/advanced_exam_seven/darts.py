from collections import deque

players_queue = deque(input().split(", "))
matrix = [input().split() for i in range(7)]

first_player = players_queue[0]
second_player = players_queue[1]
players_points_and_turns = {first_player: [501, 0], second_player: [501, 0]}
winner = ''

while True:
    current_throw = input().strip("()").split(", ")
    current_score = 0
    row = int(current_throw[0])
    col = int(current_throw[1])
    player_in_turn = players_queue.popleft()
    players_queue.append(player_in_turn)
    players_points_and_turns[player_in_turn][1] += 1

    if 0 > row or row > 6:
        continue
    if 0 > col or col > 6:
        continue
    if matrix[row][col].isdigit():
        current_score = matrix[row][col]
    elif matrix[row][col] == "D":
        current_score = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
    elif matrix[row][col] == "T":
        current_score = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 3
    elif matrix[row][col] == "B":
        winner = player_in_turn
        break

    players_points_and_turns[player_in_turn][0] -= int(current_score)
    if players_points_and_turns[player_in_turn][0] <= 0:
        winner = player_in_turn
        break

if winner == first_player:
    throws = players_points_and_turns[first_player][1]
    print(f"{first_player} won the game with {throws} throws!")
elif winner == second_player:
    throws = players_points_and_turns[second_player][1]
    print(f"{second_player} won the game with {throws} throws!")
