def rectangle_area(width, height):
    area = width * height
    return area


width_rectangle = int(input())
height_rectangle = int(input())
area_rectangle = rectangle_area(width_rectangle, height_rectangle)
print(area_rectangle)
