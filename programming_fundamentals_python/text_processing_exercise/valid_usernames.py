usernames = input().split(", ")
for username in usernames:
    valid = True
    if not 3 <= len(username) <= 16:
        continue
    for ch in username:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            valid = False
            break
    if valid:
        print(username)
        