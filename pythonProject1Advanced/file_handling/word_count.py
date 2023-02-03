from re import findall

with open("words.txt", "r") as searched_words:
    searched_words = [words.split() for words in searched_words]
    words_dict = {word: 0 for word in searched_words[0]}

with open("text_one.txt", "r") as text:
    pattern = r"[a-zA-Z\']+"
    for line in text:
        words_in_the_line = findall(pattern, line)
        for word in words_in_the_line:
            word_lower = word.lower()
            if word_lower in words_dict:
                words_dict[word_lower] += 1

sorted_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
for word in sorted_dict:
    with open("output_file.txt", "a") as output:
        output.write(f"{word[0]} - {word[1]}\n")





