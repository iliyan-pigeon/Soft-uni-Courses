length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume_of_aquarium = length * width * height
volume_in_litres = volume_of_aquarium * 0.001
taken_space = volume_in_litres * (percent/100)
space_for_water = volume_in_litres - taken_space
print(space_for_water)