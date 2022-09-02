import re

messages_amount = int(input())
attacked_planets = []
destroyed_planets = []
star_pattern = r"[s, t, a, r]"
pattern = r"\@([a-zA-Z]+)[^\@\-\:\>\!]*?\:[0-9]+[^\@\-\:\>\!]*?\!([A,D])\![^\@\-\:\>\!]*?\-\>[0-9]+"
for message in range(messages_amount):
    current_message = input()
    star_matches = re.findall(star_pattern, current_message, re.IGNORECASE)
    decrypted_message = ''
    for ch in current_message:
        decrypted_message += chr(ord(ch) - len(star_matches))
    matches = re.findall(pattern, decrypted_message)
    if matches:
        if matches[0][1] == "A":
            attacked_planets.append(matches[0][0])
        elif matches[0][1] == "D":
            destroyed_planets.append(matches[0][0])
ordered_attacked = sorted(attacked_planets)
ordered_destroyed = sorted(destroyed_planets)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in ordered_attacked:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in ordered_destroyed:
    print(f"-> {planet}")

