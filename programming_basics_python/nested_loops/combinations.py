number_to_reach = int(input())
counter = 0
for first_number in range(number_to_reach + 1):
    for second_number in range(number_to_reach + 1):
        for third_number in range(number_to_reach + 1):
            if first_number + second_number + third_number == number_to_reach:
                counter += 1
print(counter)
