word = input()
list_uppercase = []
for i, d in enumerate(word):
    if d.isupper():
        list_uppercase.append(i)
print(list_uppercase)