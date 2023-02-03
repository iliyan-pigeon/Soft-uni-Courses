from collections import deque

firework_effects = deque(int(i) for i in input().split(", "))
explosive_powers = deque(int(i) for i in input().split(", "))

fireworks_dict = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
perfect_show = False

while firework_effects and explosive_powers:
    current_effect = firework_effects.popleft()
    if current_effect <= 0:
        continue
    current_power = explosive_powers.pop()
    if current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    current_firework = current_effect + current_power

    if current_firework % 3 == 0 and current_firework % 5 == 0:
        fireworks_dict["Crossette Fireworks"] += 1
    elif current_firework % 3 == 0:
        fireworks_dict["Palm Fireworks"] += 1
    elif current_firework % 5 == 0:
        fireworks_dict["Willow Fireworks"] += 1
    else:
        current_effect -= 1
        firework_effects.append(current_effect)
        explosive_powers.append(current_power)

    if fireworks_dict["Crossette Fireworks"] == 3 and fireworks_dict["Palm Fireworks"] == 3 and \
            fireworks_dict["Willow Fireworks"] == 3:
        perfect_show = True
        break

if perfect_show:
    print("Congrats! You made the perfect firework show!")
elif not perfect_show:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_powers:
    print(f" Explosive Power left: {', '.join(map(str, explosive_powers))}")

for type, amount in fireworks_dict.items():
    print(f"{type}: {amount}")
