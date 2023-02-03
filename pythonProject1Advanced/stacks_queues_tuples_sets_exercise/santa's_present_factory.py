from collections import deque

materials_stack = [int(i) for i in input().split()]
magic_levels_queue = deque(int(i) for i in input().split())
presents_crafted = {"Doll": 0,
                    "Wooden train": 0,
                    "Teddy bear": 0,
                    "Bicycle": 0}
doll = 150
wooden_train = 250
teddy_bear = 300
bicycle = 400
while materials_stack and magic_levels_queue :
    flag = False
    if materials_stack[-1] == 0:
        flag = True
        materials_stack.pop()
    if magic_levels_queue[0] == 0:
        magic_levels_queue.popleft()
        flag = True
    if flag:
        continue
    magic_level = materials_stack[-1] * magic_levels_queue[0]
    if magic_level < 0:
        materials_stack.append(materials_stack.pop() + magic_levels_queue.popleft())
    else:
        if magic_level == doll:
            presents_crafted["Doll"] += 1
            materials_stack.pop()
            magic_levels_queue.popleft()
        elif magic_level == wooden_train:
            presents_crafted["Wooden train"] += 1
            materials_stack.pop()
            magic_levels_queue.popleft()
        elif magic_level == teddy_bear:
            presents_crafted["Teddy bear"] += 1
            materials_stack.pop()
            magic_levels_queue.popleft()
        elif magic_level == bicycle:
            presents_crafted["Bicycle"] += 1
            materials_stack.pop()
            magic_levels_queue.popleft()
        else:
            materials_stack[-1] += 15
            magic_levels_queue.popleft()
if presents_crafted["Doll"] > 0 and presents_crafted["Wooden train"] > 0 or presents_crafted["Teddy bear"] > 0 and presents_crafted["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_stack:
    print("Materials left: ", end="")
    the_range = len(materials_stack)
    for i in range(the_range):
        if len(materials_stack) > 1:
            print(materials_stack.pop(), end=", ")
        else:
            print(materials_stack.pop())
if magic_levels_queue:
    print(f"Magic left: {', '.join(str(i) for i in magic_levels_queue)}")
for present, amount in sorted(presents_crafted.items()):
    if amount > 0:
        print(f"{present}: {amount}")

