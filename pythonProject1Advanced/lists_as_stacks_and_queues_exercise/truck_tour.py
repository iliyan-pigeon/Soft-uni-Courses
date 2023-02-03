from collections import deque

petrol_pumps_queue = deque()
petrol_pump_number = 0
petrol_pumps_amount = int(input())
for petrol_pump in range(petrol_pumps_amount):
    petrol_pumps_queue.append(input())
tank_amount = 0
full_circle = False
while not full_circle:
    for petrol_pump in petrol_pumps_queue:
        current_pump = petrol_pump.split()
        petrol_amount = int(current_pump[0])
        distance = int(current_pump[1])
        tank_amount += petrol_amount
        if tank_amount < distance:
            tank_amount = 0
            petrol_pump_number += 1
            petrol_pumps_queue.append(petrol_pumps_queue.popleft())
            full_circle = False
            break
        else:
            tank_amount -= distance
            full_circle = True
print(petrol_pump_number)


