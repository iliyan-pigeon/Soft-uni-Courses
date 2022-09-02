characters = input().split(", ")
ascii_dict = {}
for key in characters:
    ascii_dict[key] = ord(key)
print(ascii_dict)
