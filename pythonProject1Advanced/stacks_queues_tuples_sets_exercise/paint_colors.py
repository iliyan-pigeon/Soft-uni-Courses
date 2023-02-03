from collections import deque

color_pieces = deque(input().split())
yielded_colors = []
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
while color_pieces:
    if len(color_pieces) == 1:
        if color_pieces[0] in main_colors or color_pieces[0] in secondary_colors:
            yielded_colors.append(color_pieces.pop())
        else:
            substring = color_pieces.pop()
    else:
        combination_one = color_pieces[0] + color_pieces[-1]
        combination_two = color_pieces[-1] + color_pieces[0]
        if combination_one in main_colors or combination_one in secondary_colors:
            yielded_colors.append(combination_one)
            color_pieces.pop()
            color_pieces.popleft()
        elif combination_two in main_colors or combination_two in secondary_colors:
            yielded_colors.append(combination_two)
            color_pieces.pop()
            color_pieces.popleft()
        else:
            flag = False
            substring_one = color_pieces.pop()
            substring_two = color_pieces.popleft()
            substring_one = substring_one.replace(substring_one[-1], "", 1)
            substring_two = substring_two.replace(substring_two[-1], "", 1)
            middle_index = len(color_pieces) // 2
            if len(substring_one) > 0:
                flag = True
                color_pieces.insert(middle_index, substring_one)
            if len(substring_two) > 0:
                if flag:
                    color_pieces.insert(middle_index+1, substring_two)
                else:
                    color_pieces.insert(middle_index, substring_two)
if "orange" in yielded_colors:
    if "red" not in yielded_colors or "yellow" not in yielded_colors:
        yielded_colors.remove("orange")
if "purple" in yielded_colors:
    if "red" not in yielded_colors or "blue" not in yielded_colors:
        yielded_colors.remove("purple")
if "green" in yielded_colors:
    if "blue" not in yielded_colors or "yellow" not in yielded_colors:
        yielded_colors.remove("green")
print(yielded_colors)