encrypted_message = input()
command = input()
while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        letters_number = int(command[1])
        encrypted_message = encrypted_message[letters_number:] + encrypted_message[:letters_number]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")
