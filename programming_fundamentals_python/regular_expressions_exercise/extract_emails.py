import re

sentence = input()
pattern = r"(?<=\s)(([a-zA-Z0-9]+[a-zA-Z0-9\-\.\_]*)@([a-zA-Z\-]+)(\.[a-zA-Z\-]+)+)\b"
matches = re.findall(pattern, sentence)
for match in matches:
    print(match[0])


