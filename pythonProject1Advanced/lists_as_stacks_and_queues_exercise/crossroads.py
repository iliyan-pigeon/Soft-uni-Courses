from collections import deque

green_light_time = int(input())
free_window_time = int(input())
passed_cars = 0
crash = False
cars_queue = deque()
command = input()
while command != "END":
    green_time = green_light_time
    free_time = free_window_time
    if command == "green":
        while cars_queue:
            if green_time == 0:
                break
            current_car = cars_queue.popleft()
            current_car_queue = deque(current_car)
            while current_car_queue:
                ch = current_car_queue.popleft()
                if green_time == 0:
                    if free_time == 0:
                        crash = True
                        print("A crash happened!")
                        print(f"{current_car} was hit at {ch}.")
                        exit()
                    else:
                        free_time -= 1
                else:
                    green_time -= 1
                if not current_car_queue:
                    passed_cars += 1
    else:
        car = command
        cars_queue.append(car)
    command = input()
if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")