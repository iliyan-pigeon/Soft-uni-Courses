import re

sentence = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"
result = len(re.findall(pattern, sentence, flags=re.I))
print(result)
