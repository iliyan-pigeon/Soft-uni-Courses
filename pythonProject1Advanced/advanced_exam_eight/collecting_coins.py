rows_cols = int(input())
matrix = []
player_row = 0
player_col = 0
path_coordinates = []
collected_coins = 0
game_lost = False

for row in range(rows_cols):
    current_row = input().split()
    if "P" in current_row:
        player_row = row
        player_col = current_row.index("P")
    matrix.append(current_row)

path_coordinates.append([player_row, player_col])

while collected_coins < 100:
    command = input()

    if command == "up":
        matrix[player_row][player_col] = "."
        player_row -= 1
        if player_row < 0:
            player_row = rows_cols - 1
        path_coordinates.append([player_row, player_col])

        if matrix[player_row][player_col].isdigit():
            collected_coins += int(matrix[player_row][player_col])
        elif matrix[player_row][player_col] == "X":
            collected_coins = int(collected_coins / 2)
            game_lost = True
            break
        matrix[player_row][player_col] = "P"

    elif command == "down":
        matrix[player_row][player_col] = "."
        player_row += 1
        if player_row == rows_cols:
            player_row = 0
        path_coordinates.append([player_row, player_col])

        if matrix[player_row][player_col].isdigit():
            collected_coins += int(matrix[player_row][player_col])
        elif matrix[player_row][player_col] == "X":
            collected_coins = int(collected_coins / 2)
            game_lost = True
            break
        matrix[player_row][player_col] = "P"

    elif command == "left":
        matrix[player_row][player_col] = "."
        player_col -= 1
        if player_col < 0:
            player_col = rows_cols - 1
        path_coordinates.append([player_row, player_col])

        if matrix[player_row][player_col].isdigit():
            collected_coins += int(matrix[player_row][player_col])
        elif matrix[player_row][player_col] == "X":
            collected_coins = int(collected_coins / 2)
            game_lost = True
            break
        matrix[player_row][player_col] = "P"

    elif command == "right":
        matrix[player_row][player_col] = "."
        player_col += 1
        if player_col == rows_cols:
            player_col = 0
        path_coordinates.append([player_row, player_col])

        if matrix[player_row][player_col].isdigit():
            collected_coins += int(matrix[player_row][player_col])
        elif matrix[player_row][player_col] == "X":
            collected_coins = int(collected_coins / 2)
            game_lost = True
            break
        matrix[player_row][player_col] = "P"

if not game_lost:
    print(f"You won! You've collected {collected_coins} coins.")
elif game_lost:
    print(f"Game over! You've collected {collected_coins} coins.")

print("Your path:")
for path in path_coordinates:
    print(f"{path}")


