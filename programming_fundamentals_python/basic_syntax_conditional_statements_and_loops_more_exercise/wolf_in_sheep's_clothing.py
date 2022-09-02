animals = input()
my_list = animals.split()
danger_place = 0
sheep_number = 0
if my_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    def reverse(lst):
        lst.reverse()
        return lst
    for animal in (reverse(my_list)):
        if animal == "sheep" or animal == "sheep,":
            sheep_number += 1
        else:
            break
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")