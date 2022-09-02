numbers = [int(number) for number in input().split(" ")]
middle_index = len(numbers) // 2
first_car = numbers[:middle_index]
second_car = numbers[-1:middle_index:-1]
first_car_total = 0
second_car_total = 0
for time in first_car:
    if time != 0:
        first_car_total += time
    elif time == 0:
        if len(first_car) > 0:
            first_car_total *= 0.8
        elif len(second_car) == 0:
            pass
for time in second_car:
    if time != 0:
        second_car_total += time
    elif time == 0:
        if len(second_car) > 0:
            second_car_total *= 0.8
        elif len(second_car) == 0:
            pass
if first_car_total < second_car_total and first_car_total > 0:
    print(f"The winner is left with total time: {first_car_total:.1f}")
elif first_car_total > second_car_total and second_car_total > 0:
    print(f"The winner is right with total time: {second_car_total:.1f}")
