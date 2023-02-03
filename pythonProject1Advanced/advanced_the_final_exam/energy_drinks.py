from collections import deque

caffeine_milligrams = [int(i) for i in input().split(", ")]
energy_drinks = deque(int(i) for i in input().split(", "))

consumed_caffeine = 0
max_caffeine = 300

while caffeine_milligrams and energy_drinks:
    current_milligrams = caffeine_milligrams.pop()
    current_drink = energy_drinks.popleft()
    current_caffeine = current_milligrams * current_drink

    if consumed_caffeine + current_caffeine <= max_caffeine:
        consumed_caffeine += current_caffeine

    else:
        energy_drinks.append(current_drink)
        consumed_caffeine -= 30

        if consumed_caffeine < 0:
            consumed_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
elif not energy_drinks:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {consumed_caffeine} mg caffeine.")
