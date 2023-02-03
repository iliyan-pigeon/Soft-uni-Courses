from collections import deque

cups_queue = deque(int(i) for i in input().split())
bottles_stack = [int(i) for i in input().split()]
wasted_water = 0
while cups_queue:
    if bottles_stack:
        current_bottle = bottles_stack.pop()
        if current_bottle >= cups_queue[0]:
            difference = abs(current_bottle - cups_queue.popleft())
            wasted_water += difference
        elif current_bottle < cups_queue[0]:
            cups_queue[0] -= current_bottle
    elif not bottles_stack:
        break
if bottles_stack:
    print("Bottles: ", end="")
    for bottle in bottles_stack[::-1]:
        print(f"{bottle} ", end="")
elif cups_queue:
    print(f"Cups: ", end="")
    for cup in cups_queue:
        print(f"{cup} ", end="")
print(f"\nWasted litters of water: {wasted_water}")