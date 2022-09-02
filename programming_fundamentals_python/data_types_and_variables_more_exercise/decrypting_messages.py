key = int(input())
number = int(input())
message_list = []
for i in range(number):
    character = input()
    new_character = chr(ord(character) + key)
    message_list.append(new_character)
message = "".join(message_list)
print(message)

    