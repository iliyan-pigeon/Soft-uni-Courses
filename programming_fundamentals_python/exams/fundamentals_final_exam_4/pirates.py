cities = {}
command = input()
while command != "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in cities:
        cities[city] = {}
        cities[city]["population"] = population
        cities[city]["gold"] = gold
    elif city in cities:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    command = input()
events = input()
while events != "End":
    events = events.split("=>")
    event = events[0]
    if event == "Plunder":
        city = events[1]
        people = int(events[2])
        gold = int(events[3])
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        if cities[city]["population"] == 0 or cities[city]["gold"] == 0:
            cities.pop(city)
            print(f"{city} has been wiped off the map!")
    elif event == "Prosper":
        city = events[1]
        gold = int(events[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        elif gold > 0:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    events = input()
if len(cities) != 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, stats in cities.items():
        print(f"{city} -> Population: {stats['population']} citizens, Gold: {stats['gold']} kg")
elif len(cities) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")