heroes_number = int(input())
heroes = {}
max_hit_points = 100
max_mana_points = 200
for i in range(heroes_number):
    hero = input().split()
    the_hero = hero[0]
    hit_points = int(hero[1])
    mana_points = int(hero[2])
    heroes[the_hero] = {}
    heroes[the_hero]["hit_points"] = hit_points
    heroes[the_hero]["mana_points"] = mana_points
command = input()
while command != "End":
    command = command.split(" - ")
    the_command = command[0]
    if the_command == "CastSpell":
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero]["mana_points"] >= mp_needed:
            heroes[hero]["mana_points"] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mana_points']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif the_command == "TakeDamage":
        hero = command[1]
        damage_amount = int(command[2])
        attacker = command[3]
        heroes[hero]["hit_points"] -= damage_amount
        if heroes[hero]["hit_points"] > 0:
            print(f"{hero} was hit for {damage_amount} HP by {attacker} and now has {heroes[hero]['hit_points']} HP left!")
        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
    elif the_command == "Recharge":
        hero = command[1]
        amount = int(command[2])
        if heroes[hero]["mana_points"] + amount > max_mana_points:
            amount = max_mana_points - heroes[hero]["mana_points"]
        heroes[hero]["mana_points"] += amount
        print(f"{hero} recharged for {amount} MP!")
    elif the_command == "Heal":
        hero = command[1]
        amount = int(command[2])
        if heroes[hero]["hit_points"] + amount > max_hit_points:
            amount = max_hit_points - heroes[hero]["hit_points"]
        heroes[hero]["hit_points"] += amount
        print(f"{hero} healed for {amount} HP!")
    command = input()
for hero in heroes:
    print(hero)
    print(f"  HP: {heroes[hero]['hit_points']}")
    print(f"  MP: {heroes[hero]['mana_points']}")
