import math
first_dot_x1 = float(input())
first_dot_y1 = float(input())
first_dot_x2 = float(input())
first_dot_y2 = float(input())
second_dot_x1 = float(input())
second_dot_y1 = float(input())
second_dot_x2 = float(input())
second_dot_y2 = float(input())


def longer_line(first_x1, first_y1, first_x2, first_y2, second_x1, second_y1, second_x2, second_y2):
    first_first_dot = math.sqrt(first_x1**2 + first_y1**2)
    first_second_dot = math.sqrt(first_x2**2 + first_y2**2)
    first_difference = abs(first_first_dot - first_second_dot)
    second_first_dot = math.sqrt(second_x1**2 + second_y1**2)
    second_second_dot = math.sqrt(second_x2**2 + second_y2**2)
    second_difference = abs(second_first_dot - second_second_dot)
    result = f"({math.floor(first_x1)}, {math.floor(first_y1)})({math.floor(first_x2)}, {math.floor(first_y2)})"
    if first_first_dot > first_second_dot:
        result = f"({math.floor(first_x2)}, {math.floor(first_y2)})({math.floor(first_x1)}, {math.floor(first_y1)})"
    if first_difference < second_difference:
        result = f"({math.floor(second_x1)}, {math.floor(second_y1)})({math.floor(second_x2)}, {math.floor(second_y2)})"
        if second_first_dot > second_second_dot:
            result = f"({math.floor(second_x2)}, {math.floor(second_y2)})({math.floor(second_x1)}, {math.floor(second_y1)})"
    return result


print(longer_line(first_dot_x1, first_dot_y1, first_dot_x2, first_dot_y2, second_dot_x1, second_dot_y1, second_dot_x2, second_dot_y2))
