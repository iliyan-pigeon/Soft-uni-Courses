import re

sequence = input()
pattern = r"([\@|\#])([a-zA-Z]{3,}\1{2}[a-zA-Z]{3,})\1"
pairs = re.findall(pattern, sequence)
mirror_words = []
if not pairs:
    print(f"No word pairs found!")
elif pairs:
    print(f"{len(pairs)} word pairs found!")
    for pair in pairs:
        words = pair[1].split(f"{pair[0]}{pair[0]}")
        first_word = words[0]
        second_word = words[1]
        if first_word == second_word[::-1]:
            mirror_words.append(f"{first_word} <=> {second_word}")
if len(mirror_words) != 0:
    print("The mirror words are:")
    print(", ".join(mirror_words))
elif len(mirror_words) == 0:
    print("No mirror words!")











