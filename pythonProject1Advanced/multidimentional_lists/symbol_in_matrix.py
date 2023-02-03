rows = int(input())
matrix = []
for row in range(rows):
    matrix.append(list(input()))
searched_symbol = input()
symbol_found = False
for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_symbol:
            print(f"({row}, {col})")
            symbol_found = True
            break
    if symbol_found:
        break
if not symbol_found:
    print(f"{searched_symbol} does not occur in the matrix")
