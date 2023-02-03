sentence = input()
characters_data = {}
for ch in sentence:
    if ch not in characters_data:
        characters_data[ch] = 0
    characters_data[ch] += 1
for character, amount in sorted(characters_data.items()):
    print(f"{character}: {amount} time/s")