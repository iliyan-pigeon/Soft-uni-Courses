import re

sentence = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
matches = re.findall(pattern, sentence)
if matches:
    print(",".join(matches))
