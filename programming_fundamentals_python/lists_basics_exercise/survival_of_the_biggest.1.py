my_list = input().split(' ')
new_list = []
count = int(input())
for element in my_list:
    element_1 = int(element)
    new_list.append(element_1)
for i in range(count):
    smallest_element = min(new_list)
    my_list.remove(str(smallest_element))
    new_list.remove(smallest_element)
print(', '.join(my_list))

