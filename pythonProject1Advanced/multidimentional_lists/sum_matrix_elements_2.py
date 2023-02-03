rows, columns = [int(i) for i in input().split(", ")]
matrix = []
matrix_sum = 0
for row in range(rows):
    current_row = [int(i) for i in input().split(", ")]
    matrix.append(current_row)
    matrix_sum += sum(current_row)
print(matrix_sum)
print(matrix)
