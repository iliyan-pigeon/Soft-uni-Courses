rows, cols = map(int, input().split())
matrix = [list(input()) for row in range(rows)]
directions = list(input())

person = "P"
person_row = 0
person_col = 0
bunny_locations = []
escaped = False
died = False

for row in range(len(matrix)):
    if "P" in matrix[row]:
        person_row = row
        person_col = matrix[row].index("P")

    if "B" in matrix[row]:
        bunny_row = row
        copied_row = matrix[row].copy()
        bunny_col = 0
        while "B" in copied_row:
            bunny_col = copied_row.index("B")
            current_bunny = bunny_row, bunny_col
            bunny_locations.append(current_bunny)
            copied_row[bunny_col] = "."

for command in directions:
    bunnies_to_add = []

    if command == "U":
        if person_row - 1 < 0:
            escaped = True
            matrix[person_row][person_col] = "."
        elif matrix[person_row - 1][person_col] == "B":
            died = True
            matrix[person_row][person_col] = "."
            person_row = person_row - 1
            person_col = person_col
        elif matrix[person_row - 1][person_col] == ".":
            matrix[person_row][person_col] = "."
            person_row = person_row - 1
            person_col = person_col
            matrix[person_row][person_col] = "P"

    elif command == "D":
        if person_row + 1 == rows:
            escaped = True
            matrix[person_row][person_col] = "."
        elif matrix[person_row + 1][person_col] == "B":
            died = True
            matrix[person_row][person_col] = "."
            person_row = person_row + 1
            person_col = person_col
        elif matrix[person_row + 1][person_col] == ".":
            matrix[person_row][person_col] = "."
            person_row = person_row + 1
            person_col = person_col
            matrix[person_row][person_col] = "P"

    elif command == "R":
        if person_col + 1 == cols:
            escaped = True
            matrix[person_row][person_col] = "."
        elif matrix[person_row][person_col + 1] == "B":
            died = True
            matrix[person_row][person_col] = "."
            person_row = person_row
            person_col = person_col + 1
        elif matrix[person_row][person_col + 1] == ".":
            matrix[person_row][person_col] = "."
            person_row = person_row
            person_col = person_col + 1
            matrix[person_row][person_col] = "P"

    elif command == "L":
        if person_col - 1 < 0:
            escaped = True
            matrix[person_row][person_col] = "."
        elif matrix[person_row][person_col - 1] == "B":
            died = True
            matrix[person_row][person_col] = "."
            person_row = person_row
            person_col = person_col - 1
        elif matrix[person_row][person_col - 1] == ".":
            matrix[person_row][person_col] = "."
            person_row = person_row
            person_col = person_col - 1
            matrix[person_row][person_col] = "P"

    for bunny in bunny_locations:
        bunny_row = bunny[0]
        bunny_col = bunny[1]

        if bunny_row - 1 >= 0:
            if matrix[bunny_row - 1][bunny_col] == "P":
                died = True
            if matrix[bunny_row - 1][bunny_col] != "B":
                new_bunny = bunny_row - 1, bunny_col
                bunnies_to_add.append(new_bunny)

        if bunny_row + 1 < rows:
            if matrix[bunny_row + 1][bunny_col] == "P":
                died = True
            if matrix[bunny_row + 1][bunny_col] != "B":
                new_bunny = bunny_row + 1, bunny_col
                bunnies_to_add.append(new_bunny)

        if bunny_col + 1 < cols:
            if matrix[bunny_row][bunny_col + 1] == "P":
                died = True
            if matrix[bunny_row][bunny_col + 1] != "B":
                new_bunny = bunny_row, bunny_col + 1
                bunnies_to_add.append(new_bunny)

        if bunny_col - 1 >= 0:
            if matrix[bunny_row][bunny_col - 1] == "P":
                died = True
            if matrix[bunny_row][bunny_col - 1] != "B":
                new_bunny = bunny_row, bunny_col - 1
                bunnies_to_add.append(new_bunny)

    for bunny in bunnies_to_add:
        bunny_row = bunny[0]
        bunny_col = bunny[1]
        bunny_locations.append(bunny)
        matrix[bunny_row][bunny_col] = "B"
    bunnies_to_add.clear()

    if died or escaped:
        break

for row in matrix:
    print("".join(row))
if died:
    print(f"dead: {person_row} {person_col}")
elif escaped:
    print(f"won: {person_row} {person_col}")
