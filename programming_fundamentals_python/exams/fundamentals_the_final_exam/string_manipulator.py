characters = input()
command = input()
while command != "End":
    command = command.split()
    the_command = command[0]
    if the_command == "Translate":
        char = command[1]
        replacement = command[2]
        if char in characters:
            characters = characters.replace(char, replacement)
            print(characters)
    elif the_command == "Includes":
        substring = command[1]
        if substring in characters:
            print("True")
        elif substring not in characters:
            print("False")
    elif the_command == "Start":
        substring = command[1]
        if characters[:len(substring)] == substring:
            print("True")
        else:
            print("False")
    elif the_command == "Lowercase":
        characters = characters.lower()
        print(characters)
    elif the_command == "FindIndex":
        char = command[1]
        index = characters.rfind(char)
        print(index)
    elif the_command == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        characters = characters.replace(characters[start_index:start_index+count], "")
        print(characters)
    command = input()

