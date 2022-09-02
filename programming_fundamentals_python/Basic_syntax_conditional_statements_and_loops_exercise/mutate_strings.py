first_string = input()
second_string = input()
for symbol in range(len(first_string)):
    if first_string[symbol] != second_string[symbol]:
        s = list(first_string)
        s[symbol] = second_string[symbol]
        first_string = ''.join(s)
        print(first_string)


