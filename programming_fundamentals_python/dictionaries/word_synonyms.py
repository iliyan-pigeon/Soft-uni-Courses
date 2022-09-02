number_of_keys = int(input())
synonyms_dictionary = {}
key = ""
for i in range(1, number_of_keys*2+1):
    word = input()
    if i % 2 != 0:
        if word not in synonyms_dictionary:
            synonyms_dictionary[word] = []
        key = word
    else:
        synonyms_dictionary[key].append(word)
for key, value in synonyms_dictionary.items():
    print(f"{key} - {', '.join(value)}")

