electrons_number = int(input())
shell_number = 1
shells_list = []
while electrons_number != 0:
    current_electrons = 2 * (shell_number * shell_number)
    if electrons_number >= current_electrons:
        shells_list.append(current_electrons)
        electrons_number -= current_electrons
    else:
        shells_list.append(electrons_number)
        electrons_number = 0
    shell_number += 1
print(shells_list)
