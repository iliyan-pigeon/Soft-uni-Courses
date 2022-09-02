sentence = input()
for ch in range(len(sentence)):
    emoticon = ""
    if sentence[ch] == ":":
        emoticon += f"{sentence[ch]}{sentence[ch+1]}"
        print(emoticon)
        