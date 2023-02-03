lists = input().split("|")
flattened_list = []

for i in range(len(lists) - 1, -1, -1):
    valid = False

    for ch in lists[i]:
        if ch != " ":
            valid = True
            break

    if valid:
        flattened_list.append(" ".join(lists[i].strip().split()))

print(" ".join(flattened_list))
