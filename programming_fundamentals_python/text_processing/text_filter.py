banned_words = input().split(", ")
text = input()


def remove_banned_words(banned_list, the_text):
    for word in banned_list:
        the_text = the_text.replace(word, "*" * len(word))
    return the_text


print(remove_banned_words(banned_words, text))
