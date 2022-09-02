first_character = input()
second_character = input()
sentence = input()
gathered_characters = []
for ch in sentence:
    if ord(first_character) < ord(ch) < ord(second_character):
        gathered_characters.append(ord(ch))
print(sum(gathered_characters))
