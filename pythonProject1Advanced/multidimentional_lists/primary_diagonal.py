rows = int(input())
matrix = []
primary_diagonal_sum = 0
for row in range(rows):
    matrix.append([int(i) for i in input().split()])
for row in range(rows):
    col = row
    primary_diagonal_sum += matrix[row][col]
print(primary_diagonal_sum)

