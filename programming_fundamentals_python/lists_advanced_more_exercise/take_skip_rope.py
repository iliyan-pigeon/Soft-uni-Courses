encrypted_text = input()
numbers_list = []
symbols_list = []
result = []
for i in encrypted_text:
    if i.isnumeric():
        numbers_list.append(int(i))
    elif not i.isnumeric():
        symbols_list.append(i)
take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0]
for number in take_list:
    for i in range(number):
        result.append(symbols_list.pop(0))
    for the_number in skip_list:
        for j in range(the_number):
            symbols_list.pop(0)
        skip_list.remove(the_number)
        break
print("".join(result))
