import re

key = input().split()
type_pattern = r"\&(.+)\&"
location_pattern = r"\<(.+)\>"
command = input()
while command != "find":
    decrypted_message = ""
    index = 0
    for i in range(len(command)):
        if index == len(key):
            index = 0
        decrypted_message += chr(ord(command[i]) - int(key[index]))
        index += 1
    treasure_type = re.findall(type_pattern, decrypted_message)
    treasure_location = re.findall(location_pattern, decrypted_message)
    print(f"Found {treasure_type[0]} at {treasure_location[0]}")
    command = input()
