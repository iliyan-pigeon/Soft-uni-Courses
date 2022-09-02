numbers = [int(number) for number in input().split(", ")]
for number in numbers:
    if number == 0:
        numbers.remove(number)
        numbers.append(0)
print(numbers)
