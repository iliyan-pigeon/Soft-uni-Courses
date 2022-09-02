donations = [int(donation) for donation in input().split(", ")]
beggars_number = int(input())
beggars_outcome = []
for beggar in range(beggars_number):
    current_beggar = 0
    for donation in range(beggar, len(donations), beggars_number):
        current_beggar += donations[donation]
    beggars_outcome.append(current_beggar)
print(beggars_outcome)
