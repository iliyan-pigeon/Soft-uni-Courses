def remove_substring(substring, string):
    while substring in string:
        string = string.replace(substring, "")
    return string


word = input()
sentence = input()
result = remove_substring(word, sentence)
print(result)
