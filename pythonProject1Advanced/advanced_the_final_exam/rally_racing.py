rows_cols = int(input())
car_racing_number = input()
matrix = []
first_tunnel = []
second_tunnel = []
car_row = 0
car_col = 0
kilometers_passed = 0
disqualified = False

for row in range(rows_cols):
    current_row = input().split()
    matrix.append(current_row)

    if "T" in current_row:
        if not first_tunnel:
            first_tunnel.append(int(row))
            first_tunnel.append(int(current_row.index("T")))
        else:
            second_tunnel.append(int(row))
            second_tunnel.append(int(current_row.index("T")))

while True:
    command = input()

    if command == "End":
        disqualified = True
        matrix[car_row][car_col] = "C"
        break

    if command == "up":
        car_row -= 1

        if matrix[car_row][car_col] == ".":
            kilometers_passed += 10

        elif matrix[car_row][car_col] == "T":
            if car_row == first_tunnel[0] and car_col == first_tunnel[1]:
                car_row = second_tunnel[0]
                car_col = second_tunnel[1]
            else:
                car_row = first_tunnel[0]
                car_col = first_tunnel[1]

            matrix[first_tunnel[0]][first_tunnel[1]] = "."
            matrix[second_tunnel[0]][second_tunnel[1]] = "."
            kilometers_passed += 30

        elif matrix[car_row][car_col] == "F":
            kilometers_passed += 10
            matrix[car_row][car_col] = "C"
            break

    elif command == "down":
        car_row += 1

        if matrix[car_row][car_col] == ".":
            kilometers_passed += 10

        elif matrix[car_row][car_col] == "T":
            if car_row == first_tunnel[0] and car_col == first_tunnel[1]:
                car_row = second_tunnel[0]
                car_col = second_tunnel[1]
            else:
                car_row = first_tunnel[0]
                car_col = first_tunnel[1]

            matrix[first_tunnel[0]][first_tunnel[1]] = "."
            matrix[second_tunnel[0]][second_tunnel[1]] = "."
            kilometers_passed += 30

        elif matrix[car_row][car_col] == "F":
            kilometers_passed += 10
            matrix[car_row][car_col] = "C"
            break

    elif command == "left":
        car_col -= 1

        if matrix[car_row][car_col] == ".":
            kilometers_passed += 10

        elif matrix[car_row][car_col] == "T":
            if car_row == first_tunnel[0] and car_col == first_tunnel[1]:
                car_row = second_tunnel[0]
                car_col = second_tunnel[1]
            else:
                car_row = first_tunnel[0]
                car_col = first_tunnel[1]

            matrix[first_tunnel[0]][first_tunnel[1]] = "."
            matrix[second_tunnel[0]][second_tunnel[1]] = "."
            kilometers_passed += 30

        elif matrix[car_row][car_col] == "F":
            kilometers_passed += 10
            matrix[car_row][car_col] = "C"
            break

    elif command == "right":
        car_col += 1

        if matrix[car_row][car_col] == ".":
            kilometers_passed += 10

        elif matrix[car_row][car_col] == "T":
            if car_row == first_tunnel[0] and car_col == first_tunnel[1]:
                car_row = second_tunnel[0]
                car_col = second_tunnel[1]
            else:
                car_row = first_tunnel[0]
                car_col = first_tunnel[1]

            matrix[first_tunnel[0]][first_tunnel[1]] = "."
            matrix[second_tunnel[0]][second_tunnel[1]] = "."
            kilometers_passed += 30

        elif matrix[car_row][car_col] == "F":
            kilometers_passed += 10
            matrix[car_row][car_col] = "C"
            break

if not disqualified:
    print(f"Racing car {car_racing_number} finished the stage!")
elif disqualified:
    print(f"Racing car {car_racing_number} DNF.")

print(f"Distance covered {kilometers_passed} km." )

for row in matrix:
    print("".join(row))
