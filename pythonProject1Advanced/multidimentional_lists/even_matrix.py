rows = int(input())
jagged_array = []
for row in range(rows):
    jagged_array.append([int(i) for i in input().split(", ") if int(i) % 2 == 0])
print(jagged_array)
