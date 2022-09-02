def add_stop(sentence: str, position: int, letters: str):
    if 0 <= position < len(sentence):
        sentence = sentence[:position] + letters + sentence[position:]
    return sentence


def remove_stop(sentence: str, start_position: int, end_position: int):
    if 0 <= start_position < len(sentence) and 0 <= start_position < len(sentence):
        sentence = sentence.replace(sentence[start_position:end_position + 1], "")
    return sentence


def switch(sentence: str, old_combination: str, new_combination: str):
    if old_combination in sentence:
        sentence = sentence.replace(old_combination, new_combination)
    return sentence


locations = input()
command = input()
while command != "Travel":
    command = command.split(":")
    the_command = command[0]
    if the_command == "Add Stop":
        index = int(command[1])
        string = command[2]
        locations = add_stop(locations, index, string)
    elif the_command == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        locations = remove_stop(locations, start_index, end_index)
    elif the_command == "Switch":
        old_string = command[1]
        new_string = command[2]
        locations = switch(locations, old_string, new_string)
    print(locations)
    command = input()
print(f"Ready for world tour! Planned stops: {locations}")

