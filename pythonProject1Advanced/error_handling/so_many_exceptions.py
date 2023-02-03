numbers_list = [int(i) for i in input().split(", ")]
result = 1

for i in numbers_list:
    number = i
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)