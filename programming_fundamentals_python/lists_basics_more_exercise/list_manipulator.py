import sys

numbers_list = [int(number) for number in input().split()]
command = input()
while command != "end":
    if "exchange" in command:
        the_command = command.split()
        index = int(the_command[1])
        if index >= len(numbers_list) or index < 0:
            print("Invalid index")
        else:
            transmitter = numbers_list[index + 1:]
            numbers_list[index + 1:] = numbers_list[:index + 1]
            numbers_list[:index + 1] = transmitter
    elif "max" in command:
        if "even" in command:
            max_number = -sys.maxsize
            index_max_num = 0
            for i, d in enumerate(numbers_list):
                if d % 2 == 0:
                    if d >= max_number:
                        max_number = d
                        index_max_num = i
            if max_number == -sys.maxsize:
                print("No matches")
            else:
                print(index_max_num)
        elif "odd" in command:
            max_number = -sys.maxsize
            index_max_num = 0
            for i, d in enumerate(numbers_list):
                if d % 2 != 0:
                    if d >= max_number:
                        max_number = d
                        index_max_num = i
            if max_number == -sys.maxsize:
                print("No matches")
            else:
                print(index_max_num)
    elif "min" in command:
        if "even" in command:
            min_number = sys.maxsize
            index_min_num = 0
            for i, d in enumerate(numbers_list):
                if d % 2 == 0:
                    if d <= min_number:
                        min_number = d
                        index_min_num = i
            if min_number == sys.maxsize:
                print("No matches")
            else:
                print(index_min_num)
        elif "odd" in command:
            min_number = sys.maxsize
            index_min_num = 0
            for i, d in enumerate(numbers_list):
                if d % 2 != 0:
                    if d <= min_number:
                        min_number = d
                        index_min_num = i
            if min_number == sys.maxsize:
                print("No matches")
            else:
                print(index_min_num)
    elif "first" in command:
        elements_list = []
        the_command = command.split()
        elements_needed = int(the_command[1])
        if elements_needed > len(numbers_list):
            print("Invalid count")
        elif "even" in command:
            for number in numbers_list:
                if len(elements_list) >= elements_needed:
                    break
                if number % 2 == 0:
                    elements_list.append(number)
            print(elements_list)
        elif "odd" in command:
            for number in numbers_list:
                if len(elements_list) >= elements_needed:
                    break
                if number % 2 != 0:
                    elements_list.append(number)
            print(elements_list)
    elif "last" in command:
        elements_list = []
        the_command = command.split()
        elements_needed = int(the_command[1])
        if elements_needed > len(numbers_list):
            print("Invalid count")
        elif "even" in command:
            for number in numbers_list:
                if number % 2 == 0:
                    elements_list.append(number)
                if len(elements_list) > elements_needed:
                    elements_list.pop(0)
            print(elements_list)
        elif "odd" in command:
            for number in numbers_list:
                if number % 2 != 0:
                    elements_list.append(number)
                if len(elements_list) > elements_needed:
                    elements_list.pop(0)
            print(elements_list)
    command = input()
print(numbers_list)