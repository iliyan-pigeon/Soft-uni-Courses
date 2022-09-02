start = int(input())
finish = int(input())
number_to_reach = int(input())
combinations = 0
matches = 0
for first_number in range(start, finish + 1):
    for second_number in range(start, finish + 1):
        combinations += 1
        if first_number + second_number == number_to_reach:
            matches += 1
            print(f"Combination N:{combinations} ({first_number} + {second_number} = {number_to_reach})")
            exit()
if matches == 0:
    print(f"{combinations} combinations - neither equals {number_to_reach}")