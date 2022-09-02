import sys

number = int(input())
biggest_number = -sys.maxsize
smallest_number = sys.maxsize
for number in range(number):
    value = int(input())
    if value >= biggest_number:
        biggest_number = value
    if value <= smallest_number:
        smallest_number = value
print(f"Max number: {biggest_number}")
print(f"Min number: {smallest_number}")
