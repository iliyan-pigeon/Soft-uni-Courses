command = input()
to_do_list = ["0"] * 10
while command != "End":
    command = command.split("-")
    index_importance = int(command[0]) - 1
    task = command[1]
    to_do_list.pop(index_importance)
    to_do_list.insert(index_importance, task)
    command = input()
while "0" in to_do_list:
    index = to_do_list.index("0")
    to_do_list.pop(index)
print(to_do_list)


