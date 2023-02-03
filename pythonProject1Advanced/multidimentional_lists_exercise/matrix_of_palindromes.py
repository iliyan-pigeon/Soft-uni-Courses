rows, cols = [int(i) for i in input().split()]
matrix = []
for row in range(rows):
    current_row = ''
    for col in range(cols):
        current_row += chr(97 + row) + chr(97 + row + col) + chr(97 + row) + " "
    matrix.append(current_row)
    current_row = ''
for row in matrix:
    print(row)


