def multiply_words(some_list):
    result = "".join([word * len(word) for word in some_list])
    return result


strings = input().split()
print(multiply_words(strings))
