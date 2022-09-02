numbers = map(int, input().split())
int_numbers = []
for number in numbers:
    int_numbers.append(int(number))
print(f"The minimum number is {min(int_numbers)}")
print(f"The maximum number is {max(int_numbers)}")
print(f"The sum number is: {sum(int_numbers)}")
