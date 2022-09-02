sentence = input()
emoticons = []
emoticon = ""
finish_it = False
for ch in sentence:
    if ch == ":":
        emoticon += ch
        finish_it = True
    elif finish_it:
        emoticon += ch
        finish_it = False
        emoticons.append(emoticon)
        emoticon = ""
for i in emoticons:
    print(i)

