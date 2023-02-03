def rover_position(matrix):
    row = 0
    col = 0
    for i in range(len(matrix)):
        if "E" in matrix[i]:
            row = i
            col = matrix[i].index("E")
    return row, col


matrix_mars = [input().split() for i in range(6)]
commands_list = input().split(", ")

rover_row, rover_col = rover_position(matrix_mars)
water_amount = 0
metal_amount = 0
concrete_amount = 0

for command in commands_list:
    if command == "up":
        if rover_row - 1 < 0:
            rover_row = 5
        else:
            rover_row -= 1
    elif command == "down":
        if rover_row + 1 > 5:
            rover_row = 0
        else:
            rover_row += 1
    elif command == "left":
        if rover_col - 1 < 0:
            rover_col = 5
        else:
            rover_col -= 1
    elif command == "right":
        if rover_col + 1 > 5:
            rover_col = 0
        else:
            rover_col += 1

    if matrix_mars[rover_row][rover_col] == "W":
        water_amount += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif matrix_mars[rover_row][rover_col] == "M":
        metal_amount += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif matrix_mars[rover_row][rover_col] == "C":
        concrete_amount += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif matrix_mars[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water_amount and metal_amount and concrete_amount:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")



