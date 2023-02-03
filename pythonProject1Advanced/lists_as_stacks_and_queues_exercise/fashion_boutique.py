clothes_stack = [int(i) for i in input().split()]
rack_capacity = int(input())
current_rack = 0
racks_amount = 1
while clothes_stack:
    current_wear = clothes_stack.pop()
    if current_rack + current_wear > rack_capacity:
        racks_amount += 1
        current_rack = 0
        current_rack += current_wear
    else:
        current_rack += current_wear
print(racks_amount)