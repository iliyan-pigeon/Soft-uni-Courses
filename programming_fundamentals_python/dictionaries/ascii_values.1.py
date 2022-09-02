characters = input().split(", ")
ascii_dict = {key: ord(key) for key in characters}
print(ascii_dict)