initial_string = list(input())
rows_cols = int(input())
matrix = []
player_row = 0
player_col = 0

for row in range(rows_cols):
    current_row = list(input())
    if "P" in current_row:
        player_row = row
        player_col = current_row.index("P")
    matrix.append(current_row)

commands_amount = int(input())

for i in range(commands_amount):
    command = input()

    if command == "up":
        if player_row - 1 < 0 and initial_string:
            initial_string.pop()
        else:
            matrix[player_row][player_col] = "-"
            player_row -= 1
            if matrix[player_row][player_col].isalpha():
                initial_string.append(matrix[player_row][player_col])
            matrix[player_row][player_col] = "P"
    elif command == "down":
        if player_row + 1 == rows_cols and initial_string:
            initial_string.pop()
        else:
            matrix[player_row][player_col] = "-"
            player_row += 1
            if matrix[player_row][player_col].isalpha():
                initial_string.append(matrix[player_row][player_col])
            matrix[player_row][player_col] = "P"
    elif command == "left":
        if player_col - 1 < 0 and initial_string:
            initial_string.pop()
        else:
            matrix[player_row][player_col] = "-"
            player_col -= 1
            if matrix[player_row][player_col].isalpha():
                initial_string.append(matrix[player_row][player_col])
            matrix[player_row][player_col] = "P"
    elif command == "right" and initial_string:
        if player_col + 1 == rows_cols:
            initial_string.pop()
        else:
            matrix[player_row][player_col] = "-"
            player_col += 1
            if matrix[player_row][player_col].isalpha():
                initial_string.append(matrix[player_row][player_col])
            matrix[player_row][player_col] = "P"

print("".join(initial_string))
for row in matrix:
    print(''.join(row))