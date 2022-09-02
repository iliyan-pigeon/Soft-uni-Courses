numbers_list = [int(number) for number in input().split(", ")]
even_numbers_index = []
for i, d in enumerate(numbers_list):
    if d % 2 == 0:
        even_numbers_index.append(i)
print(even_numbers_index)

