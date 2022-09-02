word = input()
list_uppercase = []
for letter in word:
    if letter.isupper():
        index = word.index(letter)
        list_uppercase.append(index)
print(list_uppercase)