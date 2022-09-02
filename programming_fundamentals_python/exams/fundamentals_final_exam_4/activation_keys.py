activation_key = input()
command = input()
while command != "Generate":
    command = command.split(">>>")
    the_command = command[0]
    if the_command == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        elif substring not in activation_key:
            print(f"Substring not found!")
    elif the_command == "Flip":
        upper_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if upper_lower == "Upper":
            activation_key = f"{activation_key[:start_index]}{activation_key[start_index:end_index].upper()}{activation_key[end_index:]}"
        elif upper_lower == "Lower":
            activation_key = f"{activation_key[:start_index]}{activation_key[start_index:end_index].lower()}{activation_key[end_index:]}"
        print(activation_key)
    elif the_command == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key.replace(activation_key[start_index:end_index], "")
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")