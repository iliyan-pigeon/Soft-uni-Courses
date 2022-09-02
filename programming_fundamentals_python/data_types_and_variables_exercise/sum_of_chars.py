interval = int(input())
total_value = 0
for iteration in range(interval):
    character = input()
    total_value += ord(character)
print(f"The sum equals: {total_value}")
