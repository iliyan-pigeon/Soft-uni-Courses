presents_amount = int(input())
rows = int(input())
matrix = [input().split() for i in range(rows)]
nice_kids_amount = 0
santa_row = 0
santa_col = 0

for row in range(len(matrix)):
    if "S" in matrix[row]:
        santa_row = row
        santa_col = matrix[row].index("S")
    nice_kids_amount += matrix[row].count("V")

command = input()
while command != "Christmas morning":
    if command == "right":
        matrix[santa_row][santa_col] = "-"
        santa_col += 1
        if matrix[santa_row][santa_col] == "V":
            nice_kids_amount -= 1
            presents_amount -= 1
            if presents_amount == 0:
                matrix[santa_row][santa_col] = "S"
                break
        elif matrix[santa_row][santa_col] == "C":
            if matrix[santa_row][santa_col + 1] == "V":
                nice_kids_amount -= 1
                presents_amount -= 1
                matrix[santa_row][santa_col + 1] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row - 1][santa_col] == "V":
                nice_kids_amount -= 1
                presents_amount -= 1
                matrix[santa_row - 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row + 1][santa_col] == "V":
                nice_kids_amount -= 1
                presents_amount -= 1
                matrix[santa_row + 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row][santa_col + 1] == "X":
                presents_amount -= 1
                matrix[santa_row][santa_col + 1] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row - 1][santa_col] == "X":
                presents_amount -= 1
                matrix[santa_row - 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row + 1][santa_col] == "X":
                presents_amount -= 1
                matrix[santa_row + 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
        matrix[santa_row][santa_col] = "S"
    elif command == "left":
        matrix[santa_row][santa_col] = "-"
        santa_col -= 1
        if matrix[santa_row][santa_col] == "V":
            nice_kids_amount -= 1
            presents_amount -= 1
            if presents_amount == 0:
                matrix[santa_row][santa_col] = "S"
                break
        elif matrix[santa_row][santa_col] == "C":
            if matrix[santa_row][santa_col - 1] == "V":
                nice_kids_amount -= 1
                presents_amount -= 1
                matrix[santa_row][santa_col - 1] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row - 1][santa_col] == "V":
                nice_kids_amount -= 1
                presents_amount -= 1
                matrix[santa_row - 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row + 1][santa_col] == "V":
                nice_kids_amount -= 1
                presents_amount -= 1
                matrix[santa_row + 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row][santa_col + 1] == "X":
                presents_amount -= 1
                matrix[santa_row][santa_col + 1] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row - 1][santa_col] == "X":
                presents_amount -= 1
                matrix[santa_row - 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
            if matrix[santa_row + 1][santa_col] == "X":
                presents_amount -= 1
                matrix[santa_row + 1][santa_col] = "-"
                if presents_amount == 0:
                    matrix[santa_row][santa_col] = "S"
                    break
        matrix[santa_row][santa_col] = "S"
    elif command == "up":
        pass
    elif command == "down":
        pass
