rows = int(input())
matrix = [input().split() for row in range(rows)]
tea_is_collected = False
collected_tea = 0
alice_row = 0
alice_col = 0
for row in range(len(matrix)):
    if "A" in matrix[row]:
        alice_row = row
        alice_col = matrix[row].index("A")
        break
while True:
    command = input()
    if command == "up":
        if alice_row - 1 < 0:
            matrix[alice_row][alice_col] = "*"
            break
        elif matrix[alice_row - 1][alice_col] == "R":
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row - 1][alice_col] = "*"
            break
        elif matrix[alice_row - 1][alice_col].isdigit():
            matrix[alice_row][alice_col] = "*"
            collected_tea += int(matrix[alice_row - 1][alice_col])
            matrix[alice_row - 1][alice_col] = "A"
        else:
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row - 1][alice_col] = "A"
        alice_row = alice_row - 1
    elif command == "down":
        if alice_row + 1 > len(matrix) - 1:
            matrix[alice_row][alice_col] = "*"
            break
        elif matrix[alice_row + 1][alice_col] == "R":
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row + 1][alice_col] = "*"
            break
        elif matrix[alice_row + 1][alice_col].isdigit():
            matrix[alice_row][alice_col] = "*"
            collected_tea += int(matrix[alice_row + 1][alice_col])
            matrix[alice_row + 1][alice_col] = "A"
        else:
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row + 1][alice_col] = "A"
        alice_row = alice_row + 1
    elif command == "left":
        if alice_col - 1 < 0:
            matrix[alice_row][alice_col] = "*"
            break
        elif matrix[alice_row][alice_col - 1] == "R":
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row][alice_col - 1] = "*"
            break
        elif matrix[alice_row][alice_col - 1].isdigit():
            matrix[alice_row][alice_col] = "*"
            collected_tea += int(matrix[alice_row][alice_col - 1])
            matrix[alice_row][alice_col - 1] = "A"
        else:
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row][alice_col - 1] = "A"
        alice_col = alice_col - 1
    elif command == "right":
        if alice_col + 1 > len(matrix[0]) - 1:
            matrix[alice_row][alice_col] = "*"
            break
        elif matrix[alice_row][alice_col + 1] == "R":
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row][alice_col + 1] = "*"
            break
        elif matrix[alice_row][alice_col + 1].isdigit():
            matrix[alice_row][alice_col] = "*"
            collected_tea += int(matrix[alice_row][alice_col + 1])
            matrix[alice_row][alice_col + 1] = "A"
        else:
            matrix[alice_row][alice_col] = "*"
            matrix[alice_row][alice_col + 1] = "A"
        alice_col = alice_col + 1
    if collected_tea >= 10:
        matrix[alice_row][alice_col] = "*"
        tea_is_collected = True
        break
if tea_is_collected:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(" ".join(row))
