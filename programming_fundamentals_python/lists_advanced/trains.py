wagons_number = int(input())
wagons_list = [0] * wagons_number
command = input()
while command != "End":
    command = command.split(" ")
    the_command = command[0]
    if the_command == "add":
        people_number = int(command[-1])
        wagons_list[-1] += people_number
    elif the_command == "insert":
        index = int(command[1])
        people_number = int(command[2])
        wagons_list[index] += people_number
    elif the_command == "leave":
        index = int(command[1])
        people_number = int(command[2])
        wagons_list[index] -= people_number
    command = input()
print(wagons_list)
