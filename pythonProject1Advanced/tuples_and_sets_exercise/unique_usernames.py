usernames_amount = int(input())
usernames = set()
for name in range(usernames_amount):
    usernames.add(input())
print("\n".join(usernames))
