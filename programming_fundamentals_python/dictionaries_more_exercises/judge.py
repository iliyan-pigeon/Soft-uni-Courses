contests = {}
users_total_points = {}
current_user = input()
while current_user != "no more time":
    current_user = current_user.split(" -> ")
    username = current_user[0]
    contest = current_user[1]
    points = int(current_user[2])
    if username not in users_total_points:
        users_total_points[username] = 0
    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = points
        users_total_points[username] += points
    elif username in contests[contest]:
        if points > contests[contest][username]:
            difference = abs(points - contests[contest][username])
            users_total_points[username] += difference
            contests[contest][username] = points
    current_user = input()
for contest in contests:
    current_dict = sorted(contests[contest].items(), key=lambda kv: (-kv[1], kv[0]))
    counter = 1
    print(f"{contest}: {len(current_dict)} participants")
    for person in current_dict:
        print(f"{counter}. {person[0]} <::> {person[1]}")
        counter += 1
sorted_users = sorted(users_total_points.items(), key=lambda x: (-x[1], x[0]))
print("Individual standings:")
counter = 1
for user in sorted_users:
    print(f"{counter}. {user[0]} -> {user[1]}")
    counter += 1

