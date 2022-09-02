rows_number = int(input())
my_list = []
destroyed_ships = 0
for i in range(rows_number):
    row = [int(i) for i in input().split()]
    my_list.append(row)
battles = input().split()
for battle in battles:
    position = battle.split("-")
    row = int(position[0])
    place = int(position[1])
    if my_list[row][place] == 0:
        continue
    elif my_list[row][place] == 1:
        my_list[row][place] = 0
        destroyed_ships += 1
    elif my_list[row][place] > 1:
        my_list[row][place] -= 1
print(destroyed_ships)
