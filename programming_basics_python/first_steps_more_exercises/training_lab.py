lenght_metres = float(input())
width_metres = float(input())
corridor_width = 1
one_place_lenght = 1.2
one_place_width = 0.7
door_podium_space = 3
places_lenght = lenght_metres // one_place_lenght
places_width = (width_metres - corridor_width) // one_place_width
total_places = places_lenght * places_width - 3
print(int(total_places))