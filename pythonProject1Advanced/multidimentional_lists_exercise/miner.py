rows = int(input())
directions = input().split()
matrix = [input().split() for row in range(rows)]
miner = "s"
miner_row = 0
miner_col = 0
coal_in_matrix = 0
coal_amount_taken = 0
coal_collected = False
matrix_exit = False
for row in range(len(matrix)):
    if "s" in matrix[row]:
        miner_row = row
        miner_col = matrix[row].index("s")
    coal_in_matrix += matrix[row].count("c")
for command in directions:
    if command == "left":
        if miner_col - 1 >= 0:
            matrix[miner_row][miner_col] = "*"
            miner_col -= 1
            if matrix[miner_row][miner_col] == "c":
                coal_amount_taken += 1
            elif matrix[miner_row][miner_col] == "e":
                matrix_exit = True
                break
            matrix[miner_row][miner_col] = "s"
    elif command == "right":
        if miner_col + 1 <= len(matrix[0]) - 1:
            matrix[miner_row][miner_col] = "*"
            miner_col += 1
            if matrix[miner_row][miner_col] == "c":
                coal_amount_taken += 1
            elif matrix[miner_row][miner_col] == "e":
                matrix_exit = True
                break
            matrix[miner_row][miner_col] = "s"
    elif command == "up":
        if miner_row - 1 >= 0:
            matrix[miner_row][miner_col] = "*"
            miner_row -= 1
            if matrix[miner_row][miner_col] == "c":
                coal_amount_taken += 1
            elif matrix[miner_row][miner_col] == "e":
                matrix_exit = True
                break
            matrix[miner_row][miner_col] = "s"
    elif command == "down":
        if miner_row + 1 <= len(matrix) - 1:
            matrix[miner_row][miner_col] = "*"
            miner_row += 1
            if matrix[miner_row][miner_col] == "c":
                coal_amount_taken += 1
            elif matrix[miner_row][miner_col] == "e":
                matrix_exit = True
                break
            matrix[miner_row][miner_col] = "s"
    if coal_in_matrix == coal_amount_taken:
        coal_collected = True
        break
if not coal_collected and not matrix_exit:
    coal_left = abs(coal_in_matrix - coal_amount_taken)
    print(f"{coal_left} pieces of coal left. ({miner_row}, {miner_col})")
elif coal_collected:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif matrix_exit:
    print(f"Game over! ({miner_row}, {miner_col})")
