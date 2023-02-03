names_amount = int(input())
even_set = set()
odd_set = set()
for row in range(1, names_amount + 1):
    name = input()
    name_sum = 0
    for ch in name:
        name_sum += ord(ch)
    name_sum = int(name_sum / row)
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    elif name_sum % 2 != 0:
        odd_set.add(name_sum)
result = ''
if sum(even_set) == sum(odd_set):
    result = ", ".join(str(i) for i in odd_set.union(even_set))
elif sum(even_set) < sum(odd_set):
    result = ", ".join(str(i) for i in odd_set.difference(even_set))
elif sum(even_set) > sum(odd_set):
    result = ", ".join(str(i) for i in odd_set.symmetric_difference(even_set))
print(result)
