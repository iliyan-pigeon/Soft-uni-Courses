text = list(input())
reversed_list = []

while len(text):
    reversed_list.append(text.pop())
print(''.join(reversed_list))
