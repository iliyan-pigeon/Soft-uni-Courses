rows, cols = map(int, input().split())
counter = 0
matrix = [input().split() for row in range(rows)]
for col in range(cols-1):
    for row in range(rows - 1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            counter += 1
print(counter)
