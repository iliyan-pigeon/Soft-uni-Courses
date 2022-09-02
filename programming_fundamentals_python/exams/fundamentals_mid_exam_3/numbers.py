import sys

numbers_list = [int(number) for number in input().split()]
average_value = sum(numbers_list) / len(numbers_list)
greater_than_average = []
for number in numbers_list:
    if number > average_value:
        greater_than_average.append(number)
while len(greater_than_average) > 5:
    smallest_number = sys.maxsize
    for number in greater_than_average:
        if number < smallest_number:
            smallest_number = number
    greater_than_average.remove(smallest_number)
if len(greater_than_average) == 0:
    print("No")
else:
    result = reversed(sorted(greater_than_average))
    print(' '.join(list(map(str, result))))
