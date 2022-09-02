data_list = input().split()
command = input()
while command != "3:1":
    command = command.split()
    if command[0] == "merge":
        delete_list = []
        first_index = int(command[1])
        second_index = int(command[2])
        if first_index < 0:
            first_index = 0
        if second_index >= len(data_list):
            second_index = len(data_list)-1
        for index in range(first_index+1, second_index+1):
            data_list[first_index] += data_list[index]
            delete_list.append(data_list[index])
        for element in delete_list:
            if element in data_list:
                data_list.remove(element)
    elif command[0] == "divide":
        index = int(command[1])
        parts = int(command[2])
        element = data_list[index]
        the_range = len(data_list[index]) // parts
        while len(element) != 0:
            element = [i for i in element]
            data_list.insert(index, ''.join(element[0:the_range]))
            for i in range(the_range):
                element.pop(i)
            index += 1



    command = input()