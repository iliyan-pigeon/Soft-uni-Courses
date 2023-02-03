car_numbers = int(input())
parking_lot = set()
for car in range(car_numbers):
    direction, current_car = input().split(", ")
    if direction == "IN":
        parking_lot.add(current_car)
    elif direction == "OUT":
        parking_lot.remove(current_car)
if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")
