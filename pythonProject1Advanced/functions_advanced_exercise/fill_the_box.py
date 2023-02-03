def fill_the_box(box_height, box_length, box_width, *args):
    box_capacity = box_height * box_length * box_width
    cubes_in_box = []
    cubes_left = 0
    args = list(args)
    for arg in args:
        if arg == "Finish":
            difference = abs(sum(cubes_in_box) - box_capacity)
            return f"There is free space in the box. You could put {difference} more cubes."
        if sum(cubes_in_box) + arg <= box_capacity:
            cubes_in_box.append(arg)
        else:
            difference = abs((sum(cubes_in_box) + arg) - box_capacity)
            cubes_left += difference
            cubes_in_box.append(arg)
            for cubes in args[:-1]:
                if cubes not in cubes_in_box:
                    cubes_left += cubes
                else:
                    cubes_in_box.remove(cubes)
            return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(5, 5,
                   2, 40, 11, 7, 11, 3, 1, 5,
                   "Finish"))
