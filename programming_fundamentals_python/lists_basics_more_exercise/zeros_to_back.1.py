numbers = [str(number) for number in input().split(", ")]
new_numbers = []
for number in numbers:
    if number != "0":
        new_numbers.append(int(number))
for number in numbers:
    if number == "0":
        new_numbers.append(int(number))
print(new_numbers)