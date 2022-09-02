iterations = int(input())
list_positives = []
list_negatives = []
count_positives = 0
sum_negatives = 0
for i in range(iterations):
    number = int(input())
    if number >= 0:
        list_positives.append(number)
        count_positives += 1
    elif number < 0:
        list_negatives.append(number)
        sum_negatives += number
print(list_positives)
print(list_negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_negatives}")