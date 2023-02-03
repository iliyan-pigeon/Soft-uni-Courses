from collections import deque

matrix = [input().split() for i in range(8)]
pawns_queue = deque(["w", "b"])

white_pawn_row = 0
white_pawn_col = 0

black_pawn_row = 0
black_pawn_col = 0

for row in range(len(matrix)):
    if "w" in matrix[row]:
        white_pawn_row = row
        white_pawn_col = matrix[row].index("w")
    if "b" in matrix[row]:
        black_pawn_row = row
        black_pawn_col = matrix[row].index("b")

matrix_board = []
row = 8
for i in range(8):
    current_row = []
    col = 97
    for j in range(8):
        current_square = f"{chr(col)}{str(row)}"
        current_row.append(current_square)
        col += 1
    matrix_board.append(current_row)
    row -= 1

white_is_captured = False
black_is_captured = False
white_is_queen = False
black_is_queen = False

while True:
    pawn_in_turn = pawns_queue.popleft()
    pawns_queue.append(pawn_in_turn)

    if pawn_in_turn == "w":
        white_pawn_row -= 1
        if "8" in matrix_board[white_pawn_row][white_pawn_col]:
            white_is_queen = True
            break
        if white_pawn_row == black_pawn_row and white_pawn_col - 1 == black_pawn_col:
            black_is_captured = True
            break
        if white_pawn_row == black_pawn_row and white_pawn_col + 1 == black_pawn_col:
            black_is_captured = True
            break

    elif pawn_in_turn == "b":
        black_pawn_row += 1
        if "1" in matrix_board[black_pawn_row][black_pawn_col]:
            black_is_queen = True
            break
        if black_pawn_row == white_pawn_row and black_pawn_col + 1 == white_pawn_col:
            white_is_captured = True
            break
        if black_pawn_row == white_pawn_row and black_pawn_col - 1 == white_pawn_col:
            white_is_captured = True
            break

if white_is_queen:
    print(f"Game over! White pawn is promoted to a queen at {matrix_board[white_pawn_row][white_pawn_col]}.")
elif black_is_queen:
    print(f"Game over! Black pawn is promoted to a queen at {matrix_board[black_pawn_row][black_pawn_col]}.")
elif white_is_captured:
    print(f"Game over! Black win, capture on {matrix_board[white_pawn_row][white_pawn_col]}.")
elif black_is_captured:
    print(f"Game over! White win, capture on {matrix_board[black_pawn_row][black_pawn_col]}.")
