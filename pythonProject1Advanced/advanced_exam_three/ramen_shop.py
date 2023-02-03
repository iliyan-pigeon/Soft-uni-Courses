from collections import deque

ramen_stack = list(map(int, input().split(", ")))
people_queue = deque(map(int, input().split(", ")))

while ramen_stack and people_queue:
    current_ramen = ramen_stack.pop()
    current_person = people_queue.popleft()

    if current_ramen == current_person:
        continue
    elif current_ramen > current_person:
        current_ramen = abs(current_ramen - current_person)
        ramen_stack.append(current_ramen)
    elif current_ramen < current_person:
        current_person = abs(current_person - current_ramen)
        people_queue.appendleft(current_person)

if not people_queue:
    print("Great job! You served all the customers.")
    if ramen_stack:
        ramens_left = ", ".join(map(str, ramen_stack))
        print(f"Bowls of ramen left: {ramens_left}")
else:
    people_left = ", ".join(map(str, people_queue))
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {people_left}")
