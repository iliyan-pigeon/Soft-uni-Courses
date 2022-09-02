length_cake = int(input())
width_cake = int(input())
pieces_in_cake = length_cake * width_cake
total_pieces = 0
difference = 0
#one piece is 1*1 cm.
pieces = input()
while pieces != "STOP":
    current_pieces = int(pieces)
    total_pieces += current_pieces
    if total_pieces >= pieces_in_cake:
        break
    pieces = input()
difference = abs(total_pieces - pieces_in_cake)
if total_pieces <= pieces_in_cake:
    print(f"{difference} pieces are left.")
elif total_pieces > pieces_in_cake:
    print(f"No more cake left! You need {difference} pieces more.")