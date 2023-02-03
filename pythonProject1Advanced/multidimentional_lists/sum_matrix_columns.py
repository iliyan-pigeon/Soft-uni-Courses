rows, cols = [int(i) for i in input().split(", ")]
matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split()])
for col in range(cols):
    current_column_sum = 0
    for row in range(rows):
        current_column_sum += matrix[row][col]
    print(current_column_sum)
