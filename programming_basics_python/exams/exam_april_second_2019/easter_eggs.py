import sys

colored_eggs_number = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
the_most_color = - sys.maxsize
max_color = ""
for egg in range(colored_eggs_number):
    egg_colour = input()
    if egg_colour == "red":
        red_eggs += 1
    elif egg_colour == "orange":
        orange_eggs += 1
    elif egg_colour == "blue":
        blue_eggs += 1
    elif egg_colour == "green":
        green_eggs += 1
if red_eggs >= the_most_color:
    the_most_color = red_eggs
    max_color = "red"
if orange_eggs >= the_most_color:
    the_most_color = orange_eggs
    max_color = "orange"
if blue_eggs >= the_most_color:
    the_most_color = blue_eggs
    max_color = "blue"
if green_eggs >= the_most_color:
    the_most_color = green_eggs
    max_color = "green"
print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {the_most_color} -> {max_color}")