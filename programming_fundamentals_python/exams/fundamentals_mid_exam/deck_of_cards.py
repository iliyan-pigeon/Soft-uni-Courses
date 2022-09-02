cards_list = input().split(", ")
commands_amount = int(input())
for i in range(commands_amount):
    command = input().split(", ")
    the_command = command[0]
    if the_command == "Add":
        card_name = command[1]
        if card_name in cards_list:
            print("Card is already in the deck")
            continue
        print("Card successfully added")
        cards_list.append(card_name)
    elif the_command == "Remove":
        card_name = command[1]
        if card_name not in cards_list:
            print("Card not found")
            continue
        print("Card successfully removed")
        cards_list.remove(card_name)
    elif the_command == "Remove At":
        index = int(command[1])
        if index >= len(cards_list) or index < 0:
            print("Index out of range")
            continue
        print("Card successfully removed")
        cards_list.pop(index)
    elif the_command == "Insert":
        index = int(command[1])
        card_name = command[2]
        if index >= len(cards_list) or index < 0:
            print("Index out of range")
            continue
        if card_name in cards_list:
            print("Card is already added")
            continue
        print("Card successfully added")
        cards_list.insert(index, card_name)
print(", ".join(cards_list))
