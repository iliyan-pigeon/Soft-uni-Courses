elements_list = input().split()
moves_number = 0
command = input()
all_hit = False
while command != "end":
    invalid_index = False
    command = command.split()
    first_index = int(command[0])
    second_index = int(command[1])
    moves_number += 1
    if first_index == second_index:
        invalid_index = True
    elif first_index < 0 or second_index < 0 or first_index >= len(elements_list) or second_index >= len(elements_list):
        invalid_index = True
    elif elements_list[first_index] == elements_list[second_index]:
        element = elements_list[first_index]
        while element in elements_list:
            elements_list.remove(element)
        print(f"Congrats! You have found matching elements - {element}!")
    elif elements_list[first_index] != elements_list[second_index]:
        print("Try again!")
    if invalid_index:
        element = f"-{moves_number}a"
        index = len(elements_list) // 2
        elements_list.insert(index, element)
        elements_list.insert(index, element)
        print("Invalid input! Adding additional elements to the board")
    if len(elements_list) == 0:
        all_hit = True
        break
    command = input()
if all_hit:
    print(f"You have won in {moves_number} turns!")
elif not all_hit:
    print("Sorry you lose :(")
    print(' '.join(elements_list))

