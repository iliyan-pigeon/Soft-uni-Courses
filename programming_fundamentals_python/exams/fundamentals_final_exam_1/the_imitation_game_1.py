def move(sentence: str, number: int):
    index = number
    sentence = sentence[index:] + sentence[:index]
    return sentence


def insert(sentence: str, index: int, value: str):
    sentence = sentence[:index] + value + sentence[index:]
    return sentence


def change_all(sentence: str, substring: str, replacement: str):
    sentence = sentence.replace(substring, replacement)
    return sentence


def decrypter(sentence: str, command: str):
    command = command.split("|")
    if command[0] == "Move":
        letters_number = int(command[1])
        sentence = move(sentence, letters_number)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        sentence = insert(sentence, index, value)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        sentence = change_all(sentence, substring, replacement)
    return sentence


encrypted_message = input()
activity = input()
while activity != "Decode":
    encrypted_message = decrypter(encrypted_message, activity)
    activity = input()
print(f"The decrypted message is: {encrypted_message}")
