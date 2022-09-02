number = int(input())
key_word = input()
full_list = []
searched_list = []
for i in range(number):
    sentence = input()
    full_list.append(sentence)
for sentence in full_list:
    if key_word in sentence:
        searched_list.append(sentence)
print(full_list)
print(searched_list)