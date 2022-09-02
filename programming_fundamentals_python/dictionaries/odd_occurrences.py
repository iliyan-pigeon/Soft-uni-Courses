words = input().split()
words_dictionary = {}
for word in words:
    lower_word = word.lower()
    if lower_word not in words_dictionary:
        words_dictionary[lower_word] = 1
    elif lower_word in words_dictionary:
        words_dictionary[lower_word] += 1
for key, value in words_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")


