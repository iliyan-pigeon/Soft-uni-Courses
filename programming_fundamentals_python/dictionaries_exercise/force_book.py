forces = {}
command = input()
while command != "Lumpawaroo":
    force_side = ""
    user = ""
    if "|" in command:
        command = command.split(" | ")
        not_in = True
        force_side = command[0]
        user = command[1]
        if force_side not in forces:
            forces[force_side] = []
        for key, value in forces.items():
            if user in value:
                not_in = False
                break
        if not_in:
            forces[force_side].append(user)
    elif "->" in command:
        command = command.split(" -> ")
        force_to_change = ""
        not_in = True
        force_side = command[1]
        user = command[0]
        if force_side not in forces:
            forces[force_side] = []
        for key, value in forces.items():
            if user in value:
                not_in = False
                force_to_change = key
                break
        if not_in:
            forces[force_side].append(user)
        elif not not_in:
            forces[force_side].append(user)
            forces[force_to_change].remove(user)
        print(f"{user} joins the {force_side} side!")
    command = input()
for key, value in forces.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")

