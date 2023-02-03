names_amount = int(input())
names = set()
for name in range(names_amount):
    current_name = input()
    names.add(current_name)
for name in names:
    print(name)
