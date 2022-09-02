first_result = input()
second_result = input()
third_result = input()
wins = 0
losses = 0
draws = 0
host_result = 0
guest_result = 0
for i, d in enumerate(first_result):
    if i == 0:
        host_result = d
    elif i == 2:
        guest_result = d
if host_result > guest_result:
    wins += 1
elif host_result < guest_result:
    losses += 1
else:
        draws += 1
for i, d in enumerate(second_result):
    if i == 0:
        host_result = d
    elif i == 2:
        guest_result = d
if host_result > guest_result:
    wins += 1
elif host_result < guest_result:
    losses += 1
else:
    draws += 1
for i, d in enumerate(third_result):
    if i == 0:
        host_result = d
    elif i == 2:
        guest_result = d
if host_result > guest_result:
    wins += 1
elif host_result < guest_result:
    losses += 1
else:
    draws += 1
print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")