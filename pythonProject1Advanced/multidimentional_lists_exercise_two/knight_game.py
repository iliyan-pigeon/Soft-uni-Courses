rows = int(input())
matrix = [list(input()) for row in range(rows)]

deadliest_knight_row = 0
deadliest_knight_col = 0
highest_options = 0
removed_knights = 0

while True:
    for row in range(rows):
        for col in range(len(matrix[0])):
            current_knight_options = 0
            if matrix[row][col] == "K":
                if row + 2 <= len(matrix) - 1 and col + 1 <= len(matrix[0]) - 1:
                    if matrix[row + 2][col + 1] == "K":
                        current_knight_options += 1
                if row + 2 <= len(matrix) - 1 and col - 1 >= 0:
                    if matrix[row + 2][col - 1] == "K":
                        current_knight_options += 1
                if row - 2 >= 0 and col + 1 <= len(matrix[0]) - 1:
                    if matrix[row - 2][col + 1] == "K":
                        current_knight_options += 1
                if row - 2 >= 0 and col - 1 >= 0:
                    if matrix[row - 2][col - 1] == "K":
                        current_knight_options += 1
                if row + 1 <= len(matrix) - 1 and col + 2 <= len(matrix[0]) - 1:
                    if matrix[row + 1][col + 2] == "K":
                        current_knight_options += 1
                if row - 1 >= 0 and col + 2 <= len(matrix[0]) - 1:
                    if matrix[row - 1][col + 2] == "K":
                        current_knight_options += 1
                if row - 1 >= 0 and col - 2 >= len(matrix[0]) - 1:
                    if matrix[row - 1][col - 2] == "K":
                        current_knight_options += 1
                if row + 1 <= len(matrix) - 1 and col - 2 >= len(matrix[0]) - 1:
                    if matrix[row + 1][col - 2] == "K":
                        current_knight_options += 1
            if current_knight_options > 0:
                if current_knight_options > highest_options:
                    highest_options = current_knight_options
                    deadliest_knight_row = row
                    deadliest_knight_col = col
    if highest_options == 0:
        break
    removed_knights += 1
    matrix[deadliest_knight_row][deadliest_knight_col] = "0"
    highest_options = 0
    deadliest_knight_row = 0
    deadliest_knight_col = 0
print(removed_knights)


