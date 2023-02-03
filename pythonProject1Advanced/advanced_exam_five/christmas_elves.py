from collections import deque

elves_queue = deque(int(i) for i in input().split())
materials_stack = [int(i) for i in input().split()]

total_crafted_toys = 0
total_energy_spend = 0
cookie = 1
hot_chocolate = 2
tired_elf = False
turn = 1

while elves_queue and materials_stack or tired_elf == True:
    current_elf_energy = elves_queue.popleft()
    if current_elf_energy < 5:
        continue
    if not tired_elf:
        current_materials = materials_stack.pop()

    if turn % 3 == 0:
        if current_elf_energy >= current_materials * 2:
            total_energy_spend += current_materials * 2
            current_elf_energy -= current_materials * 2
            if turn % 5 != 0:
                total_crafted_toys += 2
                current_elf_energy += cookie
            elves_queue.append(current_elf_energy)
        else:
            current_elf_energy *= hot_chocolate
            elves_queue.append(current_elf_energy)
            tired_elf = True
            turn += 1
            continue

    else:
        if current_elf_energy >= current_materials:
            total_energy_spend += current_materials
            current_elf_energy -= current_materials
            if turn % 5 != 0:
                total_crafted_toys += 1
                current_elf_energy += cookie
            elves_queue.append(current_elf_energy)
        else:
            current_elf_energy *= hot_chocolate
            elves_queue.append(current_elf_energy)
            tired_elf = True
            turn += 1
            continue
    tired_elf = False
    turn += 1

print(f"Toys: {total_crafted_toys}")
print(f"Energy: {total_energy_spend}")
if elves_queue:
    print(f"Elves left: {', '.join(map(str, elves_queue))}")
if materials_stack:
    print(f"Boxes left: {', '.join(map(str, materials_stack))}")





