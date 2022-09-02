number = int(input())
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(number - 1, 0, -1):
    for j in range(i , 0, -1):
        print("*", end="")
    print()