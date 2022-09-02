contests_dict = {}
contest_data = input()
while contest_data != "end of contests":
    contest_data = contest_data.split(":")
    contest = contest_data[0]
    contest_password = contest_data[1]
    contests_dict[contest] = contest_password
    contest_data = input()
users_dict = {}
current_user = input()
while current_user != "end of submissions":
    current_user = current_user.split("=>")
    contest = current_user[0]
    password = current_user[1]
    username = current_user[2]
    points = int(current_user[3])
    if contest in contests_dict:
        if contests_dict[contest] == password:
            if username not in users_dict:
                users_dict[username] = {}
                users_dict[username]["total_points"] = 0
            if contest in users_dict[username]:
                if points > users_dict[username][contest]:
                    users_dict[username]["total_points"] += abs(points - users_dict[username][contest])
                    users_dict[username][contest] = points
            elif contest not in users_dict[username]:
                users_dict[username][contest] = points
                users_dict[username]["total_points"] += points
    current_user = input()
highest_score = 0
highest_scored_user = ""
for user in users_dict:
    if users_dict[user]["total_points"] > highest_score:
        highest_score = users_dict[user]["total_points"]
        highest_scored_user = user
print(f"Best candidate is {highest_scored_user} with total {highest_score} points.")
print("Ranking:")
users_list = sorted(users_dict)
for user in users_list:
    del users_dict[user]["total_points"]
    current_dict = sorted(users_dict[user].items(), key=lambda kv:
    (kv[1], kv[0]), reverse=True)
    print(user)
    for contest in current_dict:
        print(f"#  {contest[0]} -> {contest[1]}")
