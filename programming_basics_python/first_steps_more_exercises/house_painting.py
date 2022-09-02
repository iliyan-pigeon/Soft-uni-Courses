x_house_height = float(input())
y_side_wall_lenght = float(input())
h_triangle_side_height = float(input())
window_side = 1.5
door_side_a = 1.2
door_side_b = 2
window_area = window_side * window_side
windows_total_area = window_area * 2
door_area = door_side_a * door_side_b
side_wall_area = x_house_height * y_side_wall_lenght
side_walls_area = side_wall_area * 2 - windows_total_area
front_wall_area = x_house_height * x_house_height
front_back_walls_area = front_wall_area * 2 - door_area
roof_side_wall_area = x_house_height * y_side_wall_lenght
roof_side_walls_area = roof_side_wall_area * 2
roof_front_side_area = x_house_height * h_triangle_side_height / 2
roof_front_back_sides_area = roof_front_side_area * 2
walls_total_area = side_walls_area + front_back_walls_area
roof_total_area = roof_side_walls_area + roof_front_back_sides_area
green_paint = walls_total_area / 3.4
red_paint = roof_total_area / 4.3
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
