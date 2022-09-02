participants = input().split(", ")
participants_data = {}
command = input()
while command != "end of race":
    name = ""
    distance = 0
    for ch in command:
        if ch.isalpha():
            name += ch
        elif ch.isdigit():
            distance += int(ch)
    if name in participants:
        if name not in participants_data:
            participants_data[name] = 0
        participants_data[name] += distance
    command = input()
ordered_participants = sorted(participants_data.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {ordered_participants[0][0]}")
print(f"2nd place: {ordered_participants[1][0]}")
print(f"3rd place: {ordered_participants[2][0]}")

