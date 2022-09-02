number = int(input())
left_total = 0
right_total = 0
difference = 0
for i in range(number):
    value = int(input())
    left_total += value
for i in range(number):
    value = int(input())
    right_total += value
if left_total == right_total:
    print(f"Yes, sum = {left_total}")
else:
    difference = abs(left_total - right_total)
    print(f"No, diff = {difference}")