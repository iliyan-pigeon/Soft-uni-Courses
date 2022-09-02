first_number = int(input())
second_number = int(input())
first_first = int(str(first_number)[:1])
first_second = int(str(second_number)[:1])
second_first = int(str(first_number)[1:2])
second_second = int(str(second_number)[1:2])
third_first = int(str(first_number)[2:3])
third_second = int(str(second_number)[2:3])
fourth_first = int(str(first_number)[3:4])
fourth_second = int(str(second_number)[3:4])
for number_one in range(first_first, first_second+1):
    for number_two in range(second_first, second_second+1):
        for number_three in range(third_first, third_second+1):
            for number_four in range(fourth_first, fourth_second+1):
                if number_one % 2 != 0 and number_two % 2 != 0\
                    and number_three % 2 != 0 and number_four % 2 != 0:
                    print(f"{number_one}{number_two}{number_three}{number_four}", end=' ')



