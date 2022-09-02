guests = {}
unliked_meals = 0
command = input()
while command != "Stop":
    command = command.split("-")
    the_command = command[0]
    guest = command[1]
    meal = command[2]
    if the_command == "Like":
        if guest not in guests:
            guests[guest] = []
        if meal not in guests[guest]:
            guests[guest].append(meal)
    elif the_command == "Dislike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
        else:
            if meal not in guests[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                guests[guest].remove(meal)
                unliked_meals += 1
                print(f"{guest} doesn't like the {meal}.")
    command = input()
for guest in guests:
    print(f"{guest}: {', '.join(guests[guest])}")
print(f"Unliked meals: {unliked_meals}")

