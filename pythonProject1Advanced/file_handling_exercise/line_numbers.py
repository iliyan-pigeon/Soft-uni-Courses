edited_text = ''

with open("text.txt", "r") as text:
    counter = 1
    for line in text:
        numbered_line = f"Line {counter}: {line} "
        edited_text += numbered_line
        letters = 0
        punctuations = 0

        for ch in "".join(line.split()):
            if ch.isalpha():
                letters += 1
            else:
                punctuations += 1
        edited_text += f"({letters})({punctuations})\n"
        counter += 1

with open("./output.txt", "a") as output:
    output.write(edited_text)
