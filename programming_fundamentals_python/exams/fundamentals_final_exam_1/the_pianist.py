pieces_number = int(input())
pieces = {}
for i in range(pieces_number):
    piece = input().split("|")
    the_piece = piece[0]
    composer = piece[1]
    key = piece[2]
    if the_piece not in pieces:
        pieces[the_piece] = [composer, key]
command = input()
while command != "Stop":
    command = command.split("|")
    the_command = command[0]
    if the_command == "Add":
        piece = command[1]
        composer = command[2]
        new_key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        if piece not in pieces:
            pieces[piece] = [composer, new_key]
            print(f"{piece} by {composer} in {new_key} added to the collection!")
    elif the_command == "Remove":
        piece = command[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        elif piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif the_command == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
for key, value in pieces.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
