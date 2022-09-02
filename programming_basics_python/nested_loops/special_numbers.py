number = int(input())
for current in range(1111, 9999 + 1):
    should_print = True
    current_number = str(current)
    for index, digit in enumerate(current_number):
        if int(digit) == 0 or number % int(digit) != 0:
            should_print = False
            break
    if should_print:
        print(current_number, end=" ")
