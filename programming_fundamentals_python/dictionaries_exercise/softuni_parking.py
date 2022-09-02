commands_amount = int(input())
parking_data = {}
for i in range(commands_amount):
    command = input().split()
    if "register" in command:
        name = command[1]
        license_number = command[2]
        if name in parking_data:
            print(f"ERROR: already registered with plate number {parking_data[name]}")
        elif name not in parking_data:
            parking_data[name] = license_number
            print(f"{name} registered {license_number} successfully")
    elif "unregister" in command:
        name = command[1]
        if name not in parking_data:
            print(f"ERROR: user {name} not found")
        elif name in parking_data:
            parking_data.pop(name)
            print(f"{name} unregistered successfully")
for name, data in parking_data.items():
    print(f"{name} => {data}")
