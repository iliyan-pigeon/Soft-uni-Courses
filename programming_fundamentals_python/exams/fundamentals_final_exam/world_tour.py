stops_string = input()
command = input()
while command != "Travel":
    command = command.split(":")
    to_do = command[0]
    if to_do == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops_string):
            stops_string = stops_string[:index] + string + stops_string[index:]
    elif to_do == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(stops_string) and 0 <= end_index < len(stops_string):
            stops_string = stops_string.replace(stops_string[start_index:end_index+1], "")
    elif to_do == "Switch":
        old_string = command[1]
        new_string = command[2]
        stops_string = stops_string.replace(old_string, new_string)
    print(stops_string)
    command = input()
print(f"Ready for world tour! Planned stops: {stops_string}")

