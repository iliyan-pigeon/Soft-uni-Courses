items_list = input().split(", ")
command = input()
while command != "Craft!":
    command = command.split(" - ")
    action_type = command[0]
    item_type = command[1]
    if action_type == "Collect":
        if item_type not in items_list:
            items_list.append(item_type)
    elif action_type == "Drop":
        if item_type in items_list:
            items_list.remove(item_type)
    elif action_type == "Combine Items":
        items = item_type.split(":")
        first_item = items[0]
        second_item = items[1]
        if first_item in items_list:
            index = items_list.index(first_item)
            items_list.insert(index+1, second_item)
    elif action_type == "Renew":
        if item_type in items_list:
            index = items_list.index(item_type)
            items_list.append(items_list.pop(index))
    command = input()
items_string = ", ".join(items_list)
print(items_string)
