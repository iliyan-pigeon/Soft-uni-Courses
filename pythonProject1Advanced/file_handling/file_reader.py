file_path = "numbers.txt"

numbers_sum = 0
file = open(file_path)
for line in file:
    numbers_sum += int(line)

print(numbers_sum)

