positive_list = []
negative_list = []
even_list = []
odd_list = []
numbers_list = [int(number) for number in input().split(", ")]
for number in numbers_list:
    if number >= 0:
        positive_list.append(str(number))
    elif number < 0:
        negative_list.append(str(number))
    if number % 2 == 0:
        even_list.append(str(number))
    elif number % 2 != 0:
        odd_list.append(str(number))
print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")
