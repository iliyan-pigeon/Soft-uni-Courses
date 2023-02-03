matrix = [input().split() for i in range(6)]
total_points = 0

for i in range(3):
    throw_row, throw_col = [int(i) for i in input().strip("()").split(", ")]

    if throw_row < 0 or throw_row > 5:
        continue
    if throw_col < 0 or throw_col > 5:
        continue
    if matrix[throw_row][throw_col] == "B":

        for row in range(6):
            if matrix[row][throw_col].isdigit():
                total_points += int(matrix[row][throw_col])

        matrix[throw_row][throw_col] = "."

if total_points < 100:
    difference = abs(total_points - 100)
    print(f"Sorry! You need {difference} points more to win a prize.")
elif 100 <= total_points <= 199:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points <= 299:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif total_points >= 300:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
