number = int(input())
odd_total = 0
even_total = 0
difference = 0
for i in range(1, number +1):
    value = int(input())
    if i % 2 == 0:
        even_total += value
    else:
        odd_total += value
if even_total == odd_total:
    print("Yes")
    print(f"Sum = {even_total}")
elif even_total != odd_total:
    difference = abs(even_total - odd_total)
    print("No")
    print(f"Diff = {difference}")