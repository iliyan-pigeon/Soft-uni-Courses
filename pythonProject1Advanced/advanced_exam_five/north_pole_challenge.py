rows, cols = [int(i) for i in input().split(",")]
matrix = []
my_row = 0
my_col = 0
items_number = 0
decorations = 0
gifts = 0
cookies = 0
items_gathered = False

for row in range(rows):
    current_row = input().split()
    if "Y" in current_row:
        my_row = row
        my_col = current_row.index("Y")
    if "D" in current_row:
        items_number += current_row.count("D")
    if "G" in current_row:
        items_number += current_row.count("G")
    if "C" in current_row:
        items_number += current_row.count("C")
    matrix.append(current_row)

command = input()
while command != "End":
    direction = command.split("-")[0]
    steps = int(command.split("-")[1])

    for step in range(steps):
        matrix[my_row][my_col] = "x"

        if direction == "up":
            my_row -= 1
            if my_row < 0:
                my_row = rows - 1
        elif direction == "down":
            my_row += 1
            if my_row > rows - 1:
                my_row = 0
        elif direction == "left":
            my_col -= 1
            if my_col < 0:
                my_col = cols - 1
        elif direction == "right":
            my_col += 1
            if my_col > cols - 1:
                my_col = 0

        if matrix[my_row][my_col] == "D":
            decorations += 1
        elif matrix[my_row][my_col] == "G":
            gifts += 1
        elif matrix[my_row][my_col] == "C":
            cookies += 1

        matrix[my_row][my_col] = "Y"
        if decorations + gifts + cookies == items_number:
            items_gathered = True
            break

    if items_gathered:
        print("Merry Christmas!")
        break
    command = input()

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for row in matrix:
    print(" ".join(row))



