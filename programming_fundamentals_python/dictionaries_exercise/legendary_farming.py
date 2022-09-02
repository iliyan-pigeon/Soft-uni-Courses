items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while not obtained:
    materials = input().split()
    for i in range(0, len(materials), 2):
        amount = int(materials[i])
        material = materials[i+1].lower()
        if material == "shards" or material == "fragments" or material == "motes":
            items[material] += amount
        else:
            if material not in items:
                items[material] = 0
            items[material] += amount
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
for item, value in items.items():
    print(f"{item}: {value}")



