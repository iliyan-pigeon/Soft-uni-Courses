rooms_number = int(input())
enough_chairs = True
total_chairs = 0
total_people = 0
for room in range(1, rooms_number+1):
    chairs_people_info = input().split()
    current_chairs = chairs_people_info[0]
    people_number = int(chairs_people_info[1])
    if len(current_chairs) >= people_number:
        total_chairs += len(current_chairs)
        total_people += people_number
    elif len(current_chairs) < people_number:
        difference = abs(len(current_chairs) - people_number)
        print(f"{difference} more chairs needed in room {room}")
        enough_chairs = False
if enough_chairs:
    difference = abs(total_people - total_chairs)
    print(f"Game On, {difference} free chairs left")
