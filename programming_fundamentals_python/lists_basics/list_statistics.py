iterations = int(input())
list_positives = []
list_negatives = []
for i in range(iterations):
    number = int(input())
    if number >= 0:
        list_positives.append(number)
    elif number < 0:
        list_negatives.append(number)
print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}")
print(f"Sum of negatives: {sum(list_negatives)}")