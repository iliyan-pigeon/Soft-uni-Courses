matrix = []
dangerous_queens = []
king_row = 0
king_col = 0

for row in range(8):
    current_row = input().split()
    if "K" in current_row:
        king_row = row
        king_col = current_row.index("K")
    matrix.append(current_row)

searching_row = king_row
searching_col = king_col
while searching_row != 7:
    searching_row += 1
    if matrix[searching_row][king_col] == "Q":
        dangerous_queens.append([searching_row, king_col])
        break

searching_row = king_row
searching_col = king_col
while searching_row != 0:
    searching_row -= 1
    if matrix[searching_row][king_col] == "Q":
        dangerous_queens.append([searching_row, king_col])
        break

searching_row = king_row
searching_col = king_col
while searching_col != 7:
    searching_col += 1
    if matrix[king_row][searching_col] == "Q":
        dangerous_queens.append([king_row, searching_col])
        break

searching_row = king_row
searching_col = king_col
while searching_col != 0:
    searching_col -= 1
    if matrix[king_row][searching_col] == "Q":
        dangerous_queens.append([king_row, searching_col])
        break

searching_row = king_row
searching_col = king_col
while searching_row != 7 and searching_col != 7:
    searching_row += 1
    searching_col += 1
    if matrix[searching_row][searching_col] == "Q":
        dangerous_queens.append([searching_row,  searching_col])
        break

searching_row = king_row
searching_col = king_col
while searching_row != 7 and searching_col != 0:
    searching_row += 1
    searching_col -= 1
    if matrix[searching_row][searching_col] == "Q":
        dangerous_queens.append([searching_row, searching_col])
        break

searching_row = king_row
searching_col = king_col
while searching_row != 0 and searching_col != 7:
    searching_row -= 1
    searching_col += 1
    if matrix[searching_row][searching_col] == "Q":
        dangerous_queens.append([searching_row, searching_col])
        break

searching_row = king_row
searching_col = king_col
while searching_row != 0 and searching_col != 0:
    searching_row -= 1
    searching_col -= 1
    if matrix[searching_row][searching_col] == "Q":
        dangerous_queens.append([searching_row, searching_col])
        break

if dangerous_queens:
    for queen in dangerous_queens:
        print(queen)
else:
    print("The king is safe!")
