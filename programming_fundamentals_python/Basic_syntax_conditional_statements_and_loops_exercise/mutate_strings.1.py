first_string = input()
second_string = input()
last_string = first_string
for character in range(len(first_string)):
    left_side = second_string[:character+1]
    right_side = first_string[character+1:]
    current_string = left_side + right_side
    if current_string != last_string:
        print(current_string)
        last_string = current_string
