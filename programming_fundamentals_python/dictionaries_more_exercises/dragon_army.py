dragons_amount = int(input())
dragons_data = {}
for dragon in range(dragons_amount):
    current_dragon_stats = input().split()
    if "null" in current_dragon_stats:
        if current_dragon_stats[2] == "null":
            current_dragon_stats[2] = str(45)
        if current_dragon_stats[3] == "null":
            current_dragon_stats[3] = str(250)
        if current_dragon_stats[4] == "null":
            current_dragon_stats[4] = str(10)
    dragon_type = current_dragon_stats[0]
    dragon_name = current_dragon_stats[1]
    dragon_damage = int(current_dragon_stats[2])
    dragon_health = int(current_dragon_stats[3])
    dragon_armor = int(current_dragon_stats[4])
    if dragon_type not in dragons_data:
        dragons_data[dragon_type] = {}
        dragons_data[dragon_type]["total_stats"] = {"damage": 0, "health": 0, "armor": 0}
    if dragon_name not in dragons_data[dragon_type]:
        dragons_data[dragon_type][dragon_name] = {}
        dragons_data[dragon_type]["total_stats"]["damage"] += dragon_damage
        dragons_data[dragon_type]["total_stats"]["health"] += dragon_health
        dragons_data[dragon_type]["total_stats"]["armor"] += dragon_armor
    elif dragon_name in dragons_data[dragon_type]:
        if dragons_data[dragon_type][dragon_name]["damage"] < dragon_damage:
            dragons_data[dragon_type]["total_stats"]["damage"] += abs(
                dragons_data[dragon_type][dragon_name]["damage"] - dragon_damage)
        else:
            dragons_data[dragon_type]["total_stats"]["damage"] -= abs(
                dragons_data[dragon_type][dragon_name]["damage"] - dragon_damage)
        if dragons_data[dragon_type][dragon_name]["health"] < dragon_health:
            dragons_data[dragon_type]["total_stats"]["health"] += abs(
                dragons_data[dragon_type][dragon_name]["health"] - dragon_damage)
        else:
            dragons_data[dragon_type]["total_stats"]["health"] -= abs(
                dragons_data[dragon_type][dragon_name]["health"] - dragon_damage)
        if dragons_data[dragon_type][dragon_name]["armor"] < dragon_damage:
            dragons_data[dragon_type]["total_stats"]["armor"] += abs(
                dragons_data[dragon_type][dragon_name]["armor"] - dragon_damage)
        else:
            dragons_data[dragon_type]["total_stats"]["armor"] -= abs(
                dragons_data[dragon_type][dragon_name]["armor"] - dragon_damage)
    dragons_data[dragon_type][dragon_name]["damage"] = dragon_damage
    dragons_data[dragon_type][dragon_name]["health"] = dragon_health
    dragons_data[dragon_type][dragon_name]["armor"] = dragon_armor
for species, stats in dragons_data.items():
    damage = dragons_data[species]["total_stats"]["damage"] / (len(stats) - 1)
    health = dragons_data[species]["total_stats"]["health"] / (len(stats) - 1)
    armor = dragons_data[species]["total_stats"]["armor"] / (len(stats) - 1)
    print(f"{species}::({damage:.2f}/{health:.2f}/{armor:.2f})")
    dragons_data[species].pop("total_stats")
    ordered_dragons = sorted(stats, key=lambda x: x)
    for dragon in ordered_dragons:
        damage = dragons_data[species][dragon]['damage']
        health = dragons_data[species][dragon]['health']
        armor = dragons_data[species][dragon]['armor']
        print(f"-{dragon} -> damage: {damage}, health: {health}, armor: {armor}")

