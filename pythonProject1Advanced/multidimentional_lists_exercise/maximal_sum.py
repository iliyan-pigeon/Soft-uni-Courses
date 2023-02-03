import sys

rows, cols = [int(i) for i in input().split()]
matrix = [input().split() for row in range(rows)]
max_sum = -sys.maxsize
max_submatrix = []
for row in range(rows - 2):
    for col in range(cols - 2):
        current_matrix_sum = (int(matrix[row][col]) + int(matrix[row][col + 1]) + int(matrix[row][col + 2]) + \
                             int(matrix[row + 1][col]) + int(matrix[row + 1][col + 1]) + int(matrix[row + 1][col + 2]) + \
                             int(matrix[row + 2][col]) + int(matrix[row + 2][col + 1]) + int(matrix[row + 2][col + 2]))
        if current_matrix_sum > max_sum:
            max_sum = current_matrix_sum
            max_submatrix.clear()
            max_submatrix.append([matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]])
            max_submatrix.append([matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]])
            max_submatrix.append([matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]])
print(f"Sum = {max_sum}")
for row in max_submatrix:
    print(" ".join(row))


