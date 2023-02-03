with open("text.txt", "r") as text:
    unwanted_symbols = ["-", ",", ".", "!", "?"]
    counter = 0

    for line in text:
        if counter % 2 == 0:
            for ch in line:
                if ch in unwanted_symbols:
                    line = line.replace(ch, "@")

            print(" ".join(line.strip().split()[::-1]))

        counter += 1
