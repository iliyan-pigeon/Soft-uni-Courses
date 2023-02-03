matrix = [input().split() for i in range(6)]
starting_point = input().strip("()").split(", ")
row = int(starting_point[0])
col = int(starting_point[1])

command = input()
while command != "Stop":
    command = command.split(", ")
    the_command = command[0]

    if the_command == "Create":
        direction = command[1]
        value = command[2]
        if direction == "up":
            row -= 1
            if matrix[row][col] == ".":
                matrix[row][col] = value
        elif direction == "down":
            row += 1
            if matrix[row][col] == ".":
                matrix[row][col] = value
        elif direction == "left":
            col -= 1
            if matrix[row][col] == ".":
                matrix[row][col] = value
        elif direction == "right":
            col += 1
            if matrix[row][col] == ".":
                matrix[row][col] = value

    elif the_command == "Update":
        direction = command[1]
        value = command[2]
        if direction == "up":
            row -= 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value
        elif direction == "down":
            row += 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value
        elif direction == "left":
            col -= 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value
        elif direction == "right":
            col += 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value

    elif the_command == "Delete":
        direction = command[1]
        value = "."
        if direction == "up":
            row -= 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value
        elif direction == "down":
            row += 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value
        elif direction == "left":
            col -= 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value
        elif direction == "right":
            col += 1
            if matrix[row][col].isalnum():
                matrix[row][col] = value

    elif the_command == "Read":
        direction = command[1]
        if direction == "up":
            row -= 1
            if matrix[row][col].isalnum():
                print(matrix[row][col])
        elif direction == "down":
            row += 1
            if matrix[row][col].isalnum():
                print(matrix[row][col])
        elif direction == "left":
            col -= 1
            if matrix[row][col].isalnum():
                print(matrix[row][col])
        elif direction == "right":
            col += 1
            if matrix[row][col].isalnum():
                print(matrix[row][col])

    command = input()

for row in matrix:
    print(" ".join(row))
