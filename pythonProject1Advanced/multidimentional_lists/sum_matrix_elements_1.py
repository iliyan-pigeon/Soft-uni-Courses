rows, columns = [int(i) for i in input().split(", ")]
matrix = []
matrix_sum = 0
for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])
for row in range(rows):
    for column in range(columns):
        matrix_sum += matrix[row][column]
print(matrix_sum)
print(matrix)
