import sys
number_of_pairs = int(input())
sum_a = 0
sum_b = 0
sum_restart = 0
max_difference = -sys.maxsize
for pair in range(1, number_of_pairs+1):
    num = int(input())
    num_2 = int(input())
    sum_a = num + num_2
    if pair == 1:
        pass
    else:
        current_difference = abs(sum_a - sum_b)
        if max_difference < current_difference:
            max_difference = current_difference
    sum_restart = sum_b
    sum_b = sum_a
if max_difference == 0 or number_of_pairs == 1:
    if number_of_pairs == 1:
        print(f"Yes, value={sum_a}")
    else:
        print(f"Yes, value={sum_restart}")
else:
    print(f"No, maxdiff={max_difference}")

