searched_words_list = input().split(", ")
researched_words_list = input().split(", ")
final_list = []
for key_word in searched_words_list:
    for word in researched_words_list:
        if key_word in word:
            final_list.append(key_word)
            break
print(final_list)

