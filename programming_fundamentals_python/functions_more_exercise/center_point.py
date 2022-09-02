import math


def closest_point(coordinate_1, coordinate_2, coordinate_3, coordinate_4):
    first_point = math.sqrt(coordinate_1 ** 2 + coordinate_2 ** 2)
    second_point = math.sqrt(coordinate_3 ** 2 + coordinate_4 ** 2)
    result = f"({math.floor(coordinate_1)}, {math.floor(coordinate_2)})"
    if second_point < first_point:
        result = f"({math.floor(coordinate_3)}, {math.floor(coordinate_4)})"
    return result


first_metric = float(input())
second_metric = float(input())
third_metric = float(input())
fourth_metric = float(input())
result = closest_point(first_metric, second_metric, third_metric, fourth_metric)
print(result)
