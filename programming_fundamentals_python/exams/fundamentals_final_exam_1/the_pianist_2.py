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


def add(command: list, pieces: dict):
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
    return pieces


def remove(command: list, pieces: dict):
    piece = command[1]
    if piece in pieces:
        pieces.pop(piece)
        print(f"Successfully removed {piece}!")
    elif piece not in pieces:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


def change_key(command: list, pieces: dict):
    piece = command[1]
    key = command[2]
    if piece in pieces:
        pieces[piece]['key'] = key
        print(f"Changed the key of {piece} to {key}!")
    elif piece not in pieces:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


def to_print(final_pieces: dict):
    sentences = ""
    for piece, data in final_pieces.items():
        sentences += f"{piece} -> Composer: {data['composer']}, Key: {data['key']}\n"
    return sentences


pieces_number = int(input())
the_pieces = collect_pieces(pieces_number)
the_command = input()
while the_command != "Stop":
    command_info = the_command.split("|")
    current_command = command_info[0]
    if current_command == "Add":
        the_pieces = add(command_info, the_pieces)
    elif current_command == "Remove":
        the_pieces = remove(command_info, the_pieces)
    elif current_command == "ChangeKey":
        the_pieces = change_key(command_info, the_pieces)
    the_command = input()
print(to_print(the_pieces))

