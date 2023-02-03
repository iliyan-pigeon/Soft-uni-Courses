rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([i for i in map(int, input().split(" "))])
coordinates = input().split()
for coordinate in coordinates:
    current_coordinate = coordinate.split(",")
    row = int(current_coordinate[0])
    col = int(current_coordinate[1])
    if matrix[row][col] > 0:
        bomb = matrix[row][col]
        if col != 0:
            if matrix[row][col-1] > 0:
                matrix[row][col-1] -= bomb
        if col <= (len(matrix[0]) - 2):
            if matrix[row][col+1] > 0:
                matrix[row][col+1] -= bomb
        if row != 0:
            if matrix[row-1][col] > 0:
                matrix[row-1][col] -= bomb
            if col != 0:
                if matrix[row-1][col-1] > 0:
                    matrix[row-1][col-1] -= bomb
            if col <= (len(matrix[0]) - 2):
                if matrix[row-1][col+1] > 0:
                    matrix[row-1][col+1] -= bomb
        if row <= (len(matrix) - 2):
            if matrix[row+1][col] > 0:
                matrix[row+1][col] -= bomb
            if col != 0:
                if matrix[row+1][col-1] > 0:
                    matrix[row+1][col-1] -= bomb
            if col <= (len(matrix[0]) - 2):
                if matrix[row+1][col+1] > 0:
                    matrix[row+1][col+1] -= bomb
        matrix[row][col] = 0
alive_cells = [i for row in matrix for i in row if i > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(" ".join(map(str, row)))
