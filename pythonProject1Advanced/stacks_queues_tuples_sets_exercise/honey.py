from collections import deque

bees_queue = deque(int(i) for i in input().split())
nectar_stack = [int(i) for i in input().split()]
symbols_queue = deque(input().split())
total_honey = 0
while bees_queue and nectar_stack:
    if bees_queue[0] <= nectar_stack[-1]:
        current_bee = bees_queue.popleft()
        current_nectar = nectar_stack.pop()
        current_symbol = symbols_queue.popleft()
        if current_symbol == "+":
            total_honey += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            total_honey += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            total_honey += abs(current_bee * current_nectar)
        elif current_symbol == "/":
            if current_bee == 0 or current_nectar == 0:
                total_honey += 0
            else:
                total_honey += abs(current_bee / current_nectar)
    else:
        nectar_stack.pop()
print(f"Total honey made: {total_honey}")
if bees_queue:
    print(f"Bees left: {', '.join(str(i) for i in bees_queue)}")
if nectar_stack:
    print(f"Nectar left: {', '.join(str(i) for i in nectar_stack)}")

