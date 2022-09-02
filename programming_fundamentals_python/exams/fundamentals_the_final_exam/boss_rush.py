import re

number = int(input())
for i in range(number):
    current_boss = input()
    pattern = r"\|([A-Z]{4,})\|\:\#([a-zA-Z]+ [a-zA-Z]+)\#"
    data = re.findall(pattern, current_boss)
    if data:
        boss_name = data[0][0]
        boss_title = data[0][1]
        print(f"{boss_name}, The {boss_title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(boss_title)}")
    else:
        print("Access denied!")
        