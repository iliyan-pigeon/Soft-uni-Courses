gifts = input().split(' ')
command = input()
gift =''
while command != "No Money":
    if "OutOfStock" in command:
        command_1 = command.split(' ')
        gift = command_1[1]
        while gift in gifts:
            index = gifts.index(gift)
            gifts[index] = "None"
    elif "Required" in command:
        command_1 = command.split(' ')
        gift = command_1[1]
        if len(gifts)-1 >= int(command_1[2]) > 0:
            index = int(command_1[2])
            gifts[index] = gift
    elif "JustInCase" in command:
        command_1 = command.split(' ')
        gift = command_1[1]
        gifts[-1] = gift
    command = input()
while "None" in gifts:
    gifts.remove("None")
print(" ".join(gifts))