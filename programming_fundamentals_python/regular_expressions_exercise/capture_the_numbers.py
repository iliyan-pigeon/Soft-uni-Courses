import re

sentence = input()
while sentence:
    pattern = r"\d+"
    result = re.findall(pattern, sentence)
    for number in result:
        if result:
            print(number, end=" ")
    sentence = input()
