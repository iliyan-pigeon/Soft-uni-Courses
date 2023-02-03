rows = int(input())
matrix = [input().split() for row in range(rows)]
best_direction = ''
collected_positions = []
total_eggs_collected = 0
bunny_row = 0
bunny_col = 0
for row in range(rows):
    found = False
    for col in range(len(matrix[0])):
        if matrix[row][col] == "B":
            bunny_row = row
            bunny_col = col
            found = True
            break
    if found:
        break
current_eggs = 0
current_positions = []
for row in range(bunny_row, -1, -1):
    if matrix[row][bunny_col] == "X":
        break
    if matrix[row][bunny_col] != "B":
        current_eggs += int(matrix[row][bunny_col])
        current_positions.append([row, bunny_col])
if total_eggs_collected < current_eggs:
    total_eggs_collected = current_eggs
    collected_positions = current_positions
    best_direction = "up"
current_eggs = 0
current_positions = []

for row in range(bunny_row, len(matrix)):
    if matrix[row][bunny_col] == "X":
        break
    if matrix[row][bunny_col] != "B":
        current_eggs += int(matrix[row][bunny_col])
        current_positions.append([row, bunny_col])
if total_eggs_collected < current_eggs:
    total_eggs_collected = current_eggs
    collected_positions = current_positions
    best_direction = "down"
current_eggs = 0
current_positions = []
for col in range(bunny_col, len(matrix[0])):
    if matrix[bunny_row][col] == "X":
        break
    if matrix[bunny_row][col] != "B":
        current_eggs += int(matrix[bunny_row][col])
        current_positions.append([bunny_row, col])
if total_eggs_collected < current_eggs:
    total_eggs_collected = current_eggs
    collected_positions = current_positions
    best_direction = "right"
current_eggs = 0
current_positions = []
for col in range(bunny_col, -1, -1):
    if matrix[bunny_row][col] == "X":
        break
    if matrix[bunny_row][col] != "B":
        current_eggs += int(matrix[bunny_row][col])
        current_positions.append([bunny_row, col])
if total_eggs_collected < current_eggs:
    total_eggs_collected = current_eggs
    collected_positions = current_positions
    best_direction = "left"
current_eggs = 0
current_positions = []

print(best_direction)
for position in collected_positions:
    print(position)
if total_eggs_collected > 0:
    print(total_eggs_collected)
