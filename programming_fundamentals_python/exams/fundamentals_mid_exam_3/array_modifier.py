numbers_list = [int(number) for number in input().split()]
command = input()
while command != "end":
    command = command.split()
    if command[0] == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        numbers_list[first_index], numbers_list[second_index] = numbers_list[second_index], numbers_list[first_index]
    elif command[0] == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        numbers_list[first_index] = numbers_list[first_index] * numbers_list[second_index]
    elif command[0] == "decrease":
        numbers_list = [element-1 for element in numbers_list]
    command = input()
print(', '.join(list(map(str, numbers_list))))


