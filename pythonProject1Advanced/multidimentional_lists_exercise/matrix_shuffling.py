rows, cols = [int(i) for i in input().split()]
matrix = [input().split() for row in range(rows)]
command = input()
valid = True
while command != "END":
    valid = True
    if "swap" not in command or "-" in command:
        valid = False
    command = command.split()
    if len(command) != 5 or command[0] != "swap":
        valid = False
    if valid:
        row_one = int(command[1])
        col_one = int(command[2])
        row_two = int(command[3])
        col_two = int(command[4])
        if row_one > (rows - 1) or row_two > (rows - 1) or col_one > (cols - 1) or col_two > (cols - 1):
            valid = False
        if valid:
            transmitter = matrix[row_one][col_one]
            matrix[row_one][col_one] = matrix[row_two][col_two]
            matrix[row_two][col_two] = transmitter
            for row in matrix:
                print(" ".join(row))
    if not valid:
        print("Invalid input!")
    command = input()

