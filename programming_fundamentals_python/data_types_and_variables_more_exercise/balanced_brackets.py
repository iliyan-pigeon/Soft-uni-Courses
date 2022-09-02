lines_number = int(input())
brackets_counter = 0
balanced = True
for number in range(lines_number):
    character = input()
    if character == "(":
        if brackets_counter == 0:
            brackets_counter += 1
        elif brackets_counter == 1:
            balanced = False
            break
    if character == ")":
        if brackets_counter == 1:
            brackets_counter = 0
        elif brackets_counter == 0:
            balanced = False
            break
if balanced:
    print("BALANCED")
elif not balanced:
    print("UNBALANCED")


