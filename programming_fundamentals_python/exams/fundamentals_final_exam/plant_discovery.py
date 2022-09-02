flowers_number = int(input())
flowers_dict = {}
for flower in range(flowers_number):
    flower_info = input().split("<->")
    flower_type = flower_info[0]
    flower_rarity = int(flower_info[1])
    if flower_type not in flowers_dict:
        flowers_dict[flower_type] = {}
    flowers_dict[flower_type]["rarity"] = flower_rarity
command = input()
while command != "Exhibition":
    if "Rate" in command:
        command = command.split(": ")
        flower = command[1].split(" - ")[0]
        rating = int(command[1].split(" - ")[1])
        if flower not in flowers_dict:
            print("error")
        else:
            if "rating" not in flowers_dict[flower]:
                flowers_dict[flower]["rating"] = []
            flowers_dict[flower]["rating"].append(rating)
    elif "Update" in command:
        command = command.split(": ")
        flower = command[1].split(" - ")[0]
        rarity = int(command[1].split(" - ")[1])
        if flower not in flowers_dict:
            print("error")
        else:
            flowers_dict[flower]["rarity"] = rarity
    elif "Reset" in command:
        command = command.split(": ")
        flower = command[1]
        if flower not in flowers_dict:
            print("error")
        else:
            flowers_dict[flower]["rating"] = []
    command = input()
print("Plants for the exhibition:")
for key, value in flowers_dict.items():
    if "rating" in value:
        if len(value['rating']) != 0:
            print(f"- {key}; Rarity: {value['rarity']}; Rating: {(sum(value['rating']) / len(value['rating'])):.2f}")
        elif len(value['rating']) == 0:
            print(f"- {key}; Rarity: {value['rarity']}; Rating: 0.00")
    elif "rating" not in value:
        print(f"- {key}; Rarity: {value['rarity']}; Rating: 0.00")

