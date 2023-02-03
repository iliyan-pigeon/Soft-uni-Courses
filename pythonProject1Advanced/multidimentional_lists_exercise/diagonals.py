rows = int(input())
matrix = [input().split(", ") for row in range(rows)]
primary_diagonal = []
secondary_diagonal = []
secondary_col = len(matrix)-1
for row in range(rows):
    primary_col = row
    primary_diagonal.append(matrix[row][primary_col])
    secondary_diagonal.append(matrix[row][secondary_col])
    secondary_col -= 1
print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {sum(map(int, primary_diagonal))}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {sum(map(int, secondary_diagonal))}")
