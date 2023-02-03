rows_cols = int(input())
bombs_number = int(input())

matrix = []
for i in range(rows_cols):
    matrix.append(list(str(0) * rows_cols))

for bomb in range(bombs_number):
    row, col = map(int, input().strip("()").split(", "))
    matrix[row][col] = "*"

for row in range(rows_cols):
    for col in range(rows_cols):

        if matrix[row][col] != "*":
            current_number = 0

            if row - 1 >= 0:
                if matrix[row - 1][col] == "*":
                    current_number += 1
            if row + 1 < rows_cols:
                if matrix[row + 1][col] == "*":
                    current_number += 1
            if col - 1 >= 0:
                if matrix[row][col - 1] == "*":
                    current_number += 1
            if col + 1 < rows_cols:
                if matrix[row][col + 1] == "*":
                    current_number += 1
            if row - 1 >= 0 and col - 1 >= 0:
                if matrix[row - 1][col - 1] == "*":
                    current_number += 1
            if row - 1 >= 0 and col + 1 < rows_cols:
                if matrix[row - 1][col + 1] == "*":
                    current_number += 1
            if row + 1 < rows_cols and  col + 1 < rows_cols:
                if matrix[row + 1][col + 1] == "*":
                    current_number += 1
            if row + 1 < rows_cols and  col - 1 >= 0:
                if matrix[row + 1][col - 1] == "*":
                    current_number += 1

            matrix[row][col] = current_number

for row in matrix:
    print(" ".join(map(str, row)))
