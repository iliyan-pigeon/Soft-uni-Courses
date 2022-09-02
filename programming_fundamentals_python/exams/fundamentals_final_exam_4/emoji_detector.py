import re

text = input()
threshold = 1
emoji_data = {}
pattern = r"\:{2}[A-Z][a-z]{2,}\:{2}|\*{2}[A-Z][a-z]{2,}\*{2}"
for i in text:
    if i.isdigit():
        threshold *= int(i)
emojis = re.finditer(pattern, text)
for emoji in emojis:
    coolness_amount = 0
    for ch in emoji.group():
        if ch.isalpha():
            coolness_amount += int(ord(ch))
    emoji_data[emoji.group()] = coolness_amount
print(f"Cool threshold: {threshold}")
print(f"{len(emoji_data)} emojis found in the text. The cool ones are:")
for emoji, coolness in emoji_data.items():
    if coolness >= threshold:
        print(emoji)
 