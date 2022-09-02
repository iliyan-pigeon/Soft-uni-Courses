rooms_list = input().split("|")
bitcoins_amount = 0
health = 100
best_room = 0
successful_quest = True
for room in rooms_list:
    best_room += 1
    room = room.split()
    command = room[0]
    amount = int(room[1])
    current_health = health
    if command == "potion":
        current_health += amount
        if current_health > 100:
            current_health = 100
        healing_amount = abs(health - current_health)
        print(f"You healed for {healing_amount} hp.")
        health = current_health
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {amount} bitcoins.")
        bitcoins_amount += amount
    else:
        if health - amount > 0:
            print(f"You slayed {command}.")
            health -= amount
        elif health - amount <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            successful_quest = False
            break
if successful_quest:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins_amount}")
    print(f"Health: {health}")


