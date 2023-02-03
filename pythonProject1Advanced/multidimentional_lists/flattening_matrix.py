rows = int(input())
matrix = []
flattened_matrix = []
for row in range(rows):
    matrix.append(map(int, input().split(", ")))
for row in matrix:
    flattened_matrix.extend(row)
print(flattened_matrix)

