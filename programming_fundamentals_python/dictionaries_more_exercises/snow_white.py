dwarfs_data = {}
command = input()
while command != "Once upon a time":
    command = command.split(" <:> ")
    name = command[0]
    hat_colour = command[1]
    physics = int(command[2])
    current_dwarf = f"({hat_colour}) {name}"
    if current_dwarf not in dwarfs_data:
        dwarfs_data[current_dwarf] = physics
    elif current_dwarf in dwarfs_data:
        if dwarfs_data[current_dwarf] < physics:
            dwarfs_data[current_dwarf] = physics
    command = input()
ordered_dwarfs_data = sorted(dwarfs_data.items(), key=lambda x: (-x[1], x[0]))
for dwarf in ordered_dwarfs_data:
    print(f"{dwarf[0]} <-> {dwarf[1]}")

