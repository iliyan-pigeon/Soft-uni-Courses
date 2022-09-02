amounts = input().split(', ')
beggars_number = int(input())
profits = []
iteration = 0
difference = abs(len(amounts) - beggars_number)
should_add = False
if len(amounts) < beggars_number:
    should_add = True
while len(amounts) > 0:
    if amounts[0] == '':
        profits.append(0)
        break
    if beggars_number == 0:
        break
    if iteration == 0:
        for beggar in range(beggars_number):
            if beggar >= len(amounts):
                break
            profits.append(int(amounts[beggar]))
        for beggar in range(beggars_number):
            if len(amounts) == 0:
                break
            amounts.pop(0)
        iteration += 1
    elif iteration > 0 and len(amounts) > 0:
        for beggar in range(beggars_number):
            add_on_it = profits[beggar]
            to_add = amounts[beggar]
            result = int(add_on_it) + int(to_add)
            profits[beggar] = int(result)
            if len(amounts) <= 1:
                break
        for beggar in range(beggars_number):
            if len(amounts) == 0:
                break
            amounts.pop(0)
if should_add:
    for diff in range(difference):
        profits.append(0)
print(profits)
#I have 80 points on this in "Judge" system. One of the inputs is going wrong.