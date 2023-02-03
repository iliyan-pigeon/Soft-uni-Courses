first_set_length, second_set_length = tuple(map(int, input().split()))
first_set = set()
second_set = set()
for i in range(first_set_length):
    current_number = input()
    first_set.add(current_number)
for i in range(second_set_length):
    current_number = input()
    second_set.add(current_number)
matches = first_set.intersection(second_set)
print("\n".join(matches))
