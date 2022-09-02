words_list = input().split()
palindrome_word = input()
palindrome_list = []
palindrome_word_counter = 0
for word in words_list:
    if word == palindrome_word:
        palindrome_word_counter += 1
    if word == word[::-1]:
        palindrome_list.append(word)
print(palindrome_list)
print(f"Found palindrome {palindrome_word_counter} times")


