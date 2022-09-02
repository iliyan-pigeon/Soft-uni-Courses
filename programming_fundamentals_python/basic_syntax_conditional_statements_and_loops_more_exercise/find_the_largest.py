the_numbers = input()
my_list = []
rearranged_numbers = []
the_biggest = -1
for element in the_numbers:
    my_list.append(int(element))
while len(my_list) != 0:
    for number in my_list:
        if number > the_biggest:
            the_biggest = number
    my_list.remove(the_biggest)
    rearranged_numbers.append(str(the_biggest))
    the_biggest = -1
rearranged = "".join(rearranged_numbers)
print(rearranged)
