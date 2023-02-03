from collections import deque


def formatting_time(time_to_formatting):
    time_to_formatting %= (24 * 60 * 60)
    hh = time_to_formatting // 3600
    mm = (time_to_formatting % 3600) // 60
    ss = time_to_formatting % 60
    return f"{hh:02d}:{mm:02d}:{ss:02d}"


robots_info = input().split(";")
starting_time = [int(i) for i in input().split(":")]
products_queue = deque()
robots_queue = deque()
product = input()
while product != "End":
    products_queue.append(product)
    product = input()
for robot in robots_info:
    robot_name, time = robot.split("-")
    robot_data = {"name": robot_name, "processing_time": int(time), "ready_time": 0}
    robots_queue.append(robot_data)
hours, minutes, seconds = starting_time
time_in_seconds = hours * 60 * 60 + minutes * 60 + seconds
while products_queue:
    current_product = products_queue.popleft()
    time_in_seconds += 1
    found_robot = False
    for robot in robots_queue:
        if robot["ready_time"] <= time_in_seconds:
            found_robot = True
            robot["ready_time"] = time_in_seconds + robot["processing_time"]
            formatted_time = formatting_time(time_in_seconds)
            print(f"{robot['name']} - {current_product} [{formatted_time}]")
            break
    if not found_robot:
        products_queue.append(current_product)
