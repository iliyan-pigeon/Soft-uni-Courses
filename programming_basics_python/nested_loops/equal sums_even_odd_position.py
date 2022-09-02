first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    str_number = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(str_number):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=' ')
