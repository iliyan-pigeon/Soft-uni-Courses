matrix = [input().split() for row in range(5)]
targets_shot = []
targets_amount = 0
shooter_row = 0
shooter_col = 0
for row in range(len(matrix)):
    if "A" in matrix[row]:
        shooter_row = row
        shooter_col = matrix[row].index("A")
    targets_amount += matrix[row].count("x")
commands_amount = int(input())
for command in range(commands_amount):
    the_command = input().split()
    direction = the_command[1]
    if the_command[0] == "move":
        steps = int(the_command[2])
        for i in range(steps):
            if direction == "right":
                if shooter_col + 1 >= len(matrix[shooter_row]):
                    break
                elif matrix[shooter_row][shooter_col + 1] == "x":
                    break
                matrix[shooter_row][shooter_col] = "."
                shooter_col += 1
                matrix[shooter_row][shooter_col] = "A"
            elif direction == "left":
                if shooter_col - 1 < 0:
                    break
                elif matrix[shooter_row][shooter_col - 1] == "x":
                    break
                matrix[shooter_row][shooter_col] = "."
                shooter_col -= 1
                matrix[shooter_row][shooter_col] = "A"
            elif direction == "up":
                if shooter_row - 1 < 0:
                    break
                elif matrix[shooter_row - 1][shooter_col] == "x":
                    break
                matrix[shooter_row][shooter_col] = "."
                shooter_row -= 1
                matrix[shooter_row][shooter_col] = "A"
            elif direction == "down":
                if shooter_row + 1 >= len(matrix):
                    break
                elif matrix[shooter_row + 1][shooter_col] == "x":
                    break
                matrix[shooter_row][shooter_col] = "."
                shooter_row += 1
                matrix[shooter_row][shooter_col] = "A"
    elif the_command[0] == "shoot":
        if direction == "right":
            for col in range(shooter_col, len(matrix[shooter_row])):
                if matrix[shooter_row][col] == "x":
                    targets_shot.append([shooter_row, col])
                    matrix[shooter_row][col] = "."
                    break
        elif direction == "left":
            for col in range(shooter_col, -1, -1):
                if matrix[shooter_row][col] == "x":
                    targets_shot.append([shooter_row, col])
                    matrix[shooter_row][col] = "."
                    break
        elif direction == "up":
            for row in range(shooter_row, -1, -1):
                if matrix[row][shooter_col] == "x":
                    targets_shot.append([row, shooter_col])
                    matrix[row][shooter_col] = "."
                    break
        elif direction == "down":
            for row in range(shooter_row, len(matrix)):
                if matrix[row][shooter_col] == "x":
                    targets_shot.append([row, shooter_col])
                    matrix[row][shooter_col] = "."
                    break
    if targets_amount == len(targets_shot):
        break
if targets_amount == len(targets_shot):
    print(f"Training completed! All {targets_amount} targets hit.")
else:
    targets_left = abs(targets_amount - len(targets_shot))
    print(f"Training not completed! {targets_left} targets left.")
for target in targets_shot:
    print(target)





