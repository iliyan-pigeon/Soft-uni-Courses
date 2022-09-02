def between_two_characters(first, second):
    characters_list = []
    for character in range(ord(first)+1, ord(second)):
        characters_list.append(chr(character))
    return " ".join(characters_list)


first_character = input()
second_character = input()
result = between_two_characters(first_character, second_character)
print(result)
