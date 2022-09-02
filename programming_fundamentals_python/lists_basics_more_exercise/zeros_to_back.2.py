numbers = input().split(", ")
for number in numbers:
    if number == "0":
        numbers.pop(numbers.index(number))