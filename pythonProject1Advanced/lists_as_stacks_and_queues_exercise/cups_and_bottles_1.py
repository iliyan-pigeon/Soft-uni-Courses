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
to_print = ""
if bottles_stack:
    while bottles_stack:
        to_print += f" {bottles_stack.pop()}"
    print(f"Bottles:{to_print}")
elif cups_queue:
    while cups_queue:
        to_print += f" {cups_queue.popleft()}"
    print(f"Cups:{to_print}")
print(f"Wasted litters of water: {wasted_water}")