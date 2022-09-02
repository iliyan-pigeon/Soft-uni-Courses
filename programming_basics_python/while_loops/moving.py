width_space = int(input())
length_space = int(input())
height_space = int(input())
free_space = width_space * length_space * height_space
total_space_boxes = 0
difference = 0
space_is_enough = True
# one box is 1*1*1 m.
amount_boxes = input()
while amount_boxes != "Done":
    current_boxes = int(amount_boxes)
    total_space_boxes += current_boxes
    if total_space_boxes >= free_space:
        space_is_enough = False
        break
    amount_boxes = input()
difference = abs(free_space - total_space_boxes)
if space_is_enough:
    print(f"{difference} Cubic meters left.")
elif not space_is_enough:
    print(f"No more free space! You need {difference} Cubic meters more.")

