def collect_pieces(amount: int):
    pieces = {}
    for i in range(amount):
        piece = input().split("|")
        the_piece = piece[0]
        composer = piece[1]
        key = piece[2]
        pieces[the_piece] = {}
        pieces[the_piece]['composer'] = composer
        pieces[the_piece]['key'] = key
    return pieces


def operate_on_the_pieces(command: str, pieces: {}):
    while command != "Stop":
        command = command.split("|")
        current_command = command[0]
        if current_command == "Add":
            piece = command[1]
            composer = command[2]
            key = command[3]
            if piece not in pieces:
                pieces[piece] = {}
                pieces[piece]['composer'] = composer
                pieces[piece]['key'] = key
                print(f"{piece} by {composer} in {key} added to the collection!")
            elif piece in pieces:
                print(f"{piece} is already in the collection!")
        elif current_command == "Remove":
            piece = command[1]
            if piece in pieces:
                pieces.pop(piece)
                print(f"Successfully removed {piece}!")
            elif piece not in pieces:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        elif current_command == "ChangeKey":
            piece = command[1]
            key = command[2]
            if piece in pieces:
                pieces[piece]['key'] = key
                print(f"Changed the key of {piece} to {key}!")
            elif piece not in pieces:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        command = input()
    return pieces


pieces_number = int(input())
the_pieces = collect_pieces(pieces_number)
the_command = input()
final_pieces = operate_on_the_pieces(the_command, the_pieces)
for piece, data in final_pieces.items():
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")
