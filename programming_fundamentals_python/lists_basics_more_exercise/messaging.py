numbers = input().split(" ")
some_chars = input()
message = []
for number in numbers:
    combination = 0
    for i, d in enumerate(number):
        combination += int(d)
    if combination <= len(some_chars):
        for i, d in enumerate(some_chars):
            if i == combination:
                message.append(d)
                some_chars = some_chars.replace(d, "", 1)
                break
    elif combination > len(some_chars):
        index = abs(combination - len(some_chars))
        for i, d in enumerate(some_chars):
            if i == index:
                message.append(d)
                some_chars = some_chars.replace(d, "", 1)
                break
print("".join(message))