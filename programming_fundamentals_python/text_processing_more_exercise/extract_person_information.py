import re

name_pattern = r"(?<=@)([a-zA-Z]+)(?=|)"
age_pattern = r"(?<=#)(\d+)(?=\*)"
sentences_amount = int(input())
for sentence in range(sentences_amount):
    current_sentence = input()
    name = re.findall(name_pattern, current_sentence)
    age = re.findall(age_pattern, current_sentence)
    print(f"{name[0]} is {age[0]} years old.")
