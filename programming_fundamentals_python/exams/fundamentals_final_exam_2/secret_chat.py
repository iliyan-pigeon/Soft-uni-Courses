concealed_message = input()
command = input()
while command != "Reveal":
    changes = True
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
    elif command[0] == "Reverse":
        substring = command[1]
        if substring not in concealed_message:
            print("error")
            changes = False
        elif substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
    if changes:
        print(concealed_message)
    command = input()
print(f"You have a new text message: {concealed_message}")

