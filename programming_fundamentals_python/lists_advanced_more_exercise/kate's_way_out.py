my_list = []
rows_amount = int(input())
for i in range(rows_amount):
    my_list.append(input())
kate_row = ""
kate_place = ""
for row in range(len(my_list)):
    for ch in range(len(my_list[row])):
        if my_list[row][ch] == "k":
            kate_row = row
            kate_place = ch
            break
             