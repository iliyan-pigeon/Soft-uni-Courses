rows, cols = map(int, input().split())
snake_characters = input()
snake_transitioning = ''
snake_matrix = []
index = 0
for row in range(1, rows+1):
    current_row = ''
    for col in range(1, cols+1):
        if snake_transitioning == snake_characters:
            index = 0
            snake_transitioning = ''
        current_row += snake_characters[index]
        snake_transitioning += snake_characters[index]
        index += 1
    if row % 2 != 0:
        print(current_row)
    else:
        print(current_row[::-1])
