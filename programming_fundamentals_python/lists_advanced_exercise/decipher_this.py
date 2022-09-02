coded_sentence = input().split()
final_sentence = []
for sentence in coded_sentence:
    ascii_list = []
    current_sentence = []
    for character in sentence:
        if character.isdigit():
            ascii_list.append(character)
    ascii_character = int(''.join(ascii_list))
    current_sentence.append(chr(ascii_character))
    for character in sentence:
        if character.isdigit():
            pass
        else:
            current_sentence.append(character)
    current_sentence[1], current_sentence[-1] = current_sentence[-1], current_sentence[1]
    final_sentence.append("".join(current_sentence))
print(" ".join(final_sentence))

