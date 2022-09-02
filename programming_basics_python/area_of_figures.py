import math

type_of_figure = input()
if type_of_figure == 'square':
    side_a = float(input())
    area = side_a * side_a
    print(f'{area:.3f}')
elif type_of_figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')
elif type_of_figure == 'circle':
    radius = float(input())
    area = math.pi * radius * radius
    print(f'{area:.3f}')
elif type_of_figure == 'triangle':
    side_a = float(input())
    h = float(input())
    area = side_a * h / 2
    print(f'{area:.3f}')
