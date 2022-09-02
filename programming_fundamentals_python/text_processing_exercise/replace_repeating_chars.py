letters_sequence = input()
filtered_letters = ''
for letter in range(len(letters_sequence)):
    if letter == 0:
        filtered_letters += letters_sequence[letter]
    else:
        if letters_sequence[letter] != letters_sequence[letter-1]:
            filtered_letters += letters_sequence[letter]
print(filtered_letters)

