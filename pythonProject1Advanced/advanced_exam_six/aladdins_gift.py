from collections import deque

materials_values = [int(i) for i in input().split()]
magic_levels = deque(int(i) for i in input().split())
crafted_materials = {}

while materials_values and magic_levels:
    current_materials = materials_values.pop()
    current_magic = magic_levels.popleft()
    current_combination = current_materials + current_magic

    if current_combination < 100:
        if current_combination % 2 == 0:
            current_materials *= 2
            current_magic *= 3
            current_combination = current_materials + current_magic
        elif current_combination % 2 != 0:
            current_combination *= 2
    if current_combination > 499:
        current_combination /= 2
    if 100 <= current_combination <= 199:
        if "Gemstone" not in crafted_materials:
            crafted_materials["Gemstone"] = 0
        crafted_materials["Gemstone"] += 1
    if 200 <= current_combination <= 299:
        if "Porcelain Sculpture" not in crafted_materials:
            crafted_materials["Porcelain Sculpture"] = 0
        crafted_materials["Porcelain Sculpture"] += 1
    if 300 <= current_combination <= 399:
        if "Gold" not in crafted_materials:
            crafted_materials["Gold"] = 0
        crafted_materials["Gold"] += 1
    if 400 <= current_combination <= 499:
        if "Diamond Jewellery" not in crafted_materials:
            crafted_materials["Diamond Jewellery"] = 0
        crafted_materials["Diamond Jewellery"] += 1

if "Gemstone" in crafted_materials and "Porcelain Sculpture" in crafted_materials or \
    "Gold" in crafted_materials and "Diamond Jewellery" in crafted_materials:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_values:
    print(f"Materials left: {', '.join(map(str, materials_values))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

ordered_gifts = sorted(crafted_materials.items(), key=lambda x: x)

for gift in ordered_gifts:
    print(f"{gift[0]}: {gift[1]}")


