import re

participants = input().split(", ")
participants_data = {}
letters_regex = r"[a-zA-Z]+"
digits_regex = r"[1-9]"
command = input()
while command != "end of race":
    matches_letters = re.findall(letters_regex, command)
    matches_digits = re.findall(digits_regex, command)
    name = "".join(matches_letters)
    distance = sum(int(d) for d in matches_digits)
    if name in participants:
        if name not in participants_data:
            participants_data[name] = 0
        participants_data[name] += distance
    command = input()
ordered_participants = sorted(participants_data.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {ordered_participants[0][0]}")
print(f"2nd place: {ordered_participants[1][0]}")
print(f"3rd place: {ordered_participants[2][0]}")