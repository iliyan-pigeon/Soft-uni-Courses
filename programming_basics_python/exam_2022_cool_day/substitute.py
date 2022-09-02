number_k = int(input())
number_l = int(input())
number_m = int(input())
number_n = int(input())
sub = 0
for i in range(number_k, 8 + 1):
    for j in range(9, number_l - 1, -1):
        for i_two in range(number_m, 8 + 1):
            for j_two in range(9, number_n - 1, -1):
                if i_two % 2 == 0 and j_two % 2 != 0 and i % 2 == 0 and j % 2 != 0:
                    if sub >= 6:
                        exit()
                    if i_two == i and j_two == j:
                        print("Cannot change the same player.")
                    else:
                        print(f"{i}{j} - {i_two}{j_two}")
                        sub += 1