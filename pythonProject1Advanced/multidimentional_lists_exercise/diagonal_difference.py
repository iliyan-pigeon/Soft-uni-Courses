rows = int(input())
matrix = [input().split() for row in range(rows)]
primary_diagonal = []
secondary_diagonal = []
difference = 0
secondary_col = len(matrix) -1
for row in range(rows):
    primary_col = row
    primary_diagonal.append(matrix[row][primary_col])
    secondary_diagonal.append(matrix[row][secondary_col - row])
difference = abs(sum(map(int, primary_diagonal)) - sum(map(int, secondary_diagonal)))
print(difference)
