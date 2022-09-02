def store_information(number: int(), some_dictionary):
    for i in range(number):
        current_plant = input().split("<->")
        plant = current_plant[0]
        current_rarity = current_plant[1]
        if plant not in some_dictionary:
            some_dictionary[plant] = {}
        some_dictionary[plant]["rarity"] = current_rarity
        some_dictionary[plant]["rating"] = []
    return some_dictionary


def rate(some_dictionary, plant, rating):
    some_dictionary[plant]["rating"].append(rating)
    return some_dictionary


def update(some_dictionary, plant, rarity):
    some_dictionary[plant]["rarity"] = rarity
    return some_dictionary


def reset(some_dictionary, plant):
    some_dictionary[plant]["rating"] = []
    return some_dictionary


plants_amount = int(input())
plants_data = {}
plants_data = store_information(plants_amount, plants_data)
command = input()
while command != "Exhibition":
    command = command.split(": ")
    the_command = command[0]
    if the_command == "Rate":
        data = command[1].split(" - ")
        the_plant = data[0]
        rating = int(data[1])
        plants_data = rate(plants_data, the_plant, rating)
    elif the_command == "Update":
        pass
    elif the_command == "Reset":
        pass

