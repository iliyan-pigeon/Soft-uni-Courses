import sys

number_to_reach = int(input())
total_sum = 0
while total_sum < number_to_reach:
    number = int(input())
    total_sum += number
print(total_sum)
