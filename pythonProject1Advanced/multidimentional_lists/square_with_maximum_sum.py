rows, cols = [int(i) for i in input().split(", ")]
matrix = []
submatrix_highest_sum = 0
submatrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])
for col in range(cols-1):
    for row in range(rows - 1):
        current_submatrix = 0
        current_submatrix += (matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1])
        if current_submatrix > submatrix_highest_sum:
            submatrix_highest_sum = current_submatrix
            submatrix.clear()
            submatrix.append([matrix[row][col], matrix[row][col+1]])
            submatrix.append([matrix[row+1][col], matrix[row+1][col+1]])
for row in submatrix:
    print(" ".join(str(i) for i in row))
print(submatrix_highest_sum)

