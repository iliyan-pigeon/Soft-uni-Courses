from collections import deque

vowels = deque(input().split())
consonants = input().split()
flowers_dict = {"rose": "rose",
                "tulip": "tulip",
                "lotus": "lotus",
                "daffodil": "daffodil"}
found_word = ''

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key, value in flowers_dict.items():
        current_flower = value
        if current_vowel in value:
            current_flower = current_flower.replace(current_vowel, "")
        if current_consonant in value:
            current_flower = current_flower.replace(current_consonant, "")
        flowers_dict[key] = current_flower
        if current_flower == "":
            found_word = key
            break

    if found_word:
        break

if found_word:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
