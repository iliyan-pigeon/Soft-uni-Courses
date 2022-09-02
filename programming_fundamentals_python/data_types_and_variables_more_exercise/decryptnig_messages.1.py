key = int(input())
number = int(input())
message = ""
for i in range(number):
    character = input()
    new_character = chr(ord(character) + key)
    message += new_character
print(message)
