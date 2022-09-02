number = int(input())
is_happy = False
while not is_happy:
    number += 1
    my_list = []
    for i, d in enumerate(str(number)):
        if d not in my_list:
            my_list += d
        else:
            break
    if len(str(number)) == len(my_list):
        is_happy = True
    if is_happy:
        print("".join(my_list))
        break