rows = int(input())
matrix = [input().split() for row in range(rows)]
for row in range(len(matrix)):
    matrix[row] = [int(i) for i in matrix[row]]
command = input()
while command != "END":
    command = command.split()
    the_command = command[0]
    row = int(command[1])
    col = int(command[2])
    amount = int(command[3])
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]):
        if the_command == "Add":
            matrix[row][col] += amount
        elif the_command == "Subtract":
            matrix[row][col] -= amount
    else:
        print("Invalid coordinates")
    command = input()
for row in matrix:
    print(" ".join(map(str, row)))

