eggs_size = input()
eggs_colour = input()
batches_number = int(input())
batch_price = 0
manufacturing_costs = 0
brut_price = 0
net_price = 0
if eggs_size == "Large":
    if eggs_colour == "Red":
        batch_price = 16
    elif eggs_colour == "Green":
        batch_price = 12
    elif eggs_colour == "Yellow":
        batch_price = 9
elif eggs_size == "Medium":
    if eggs_colour == "Red":
        batch_price = 13
    elif eggs_colour == "Green":
        batch_price = 9
    elif eggs_colour == "Yellow":
        batch_price = 7
elif eggs_size == "Small":
    if eggs_colour == "Red":
        batch_price = 9
    elif eggs_colour == "Green":
        batch_price = 8
    elif eggs_colour == "Yellow":
        batch_price = 5
brut_price = batch_price * batches_number
manufacturing_costs = brut_price * 0.35
net_price = brut_price - manufacturing_costs
print(f"{net_price:.2f} leva.")