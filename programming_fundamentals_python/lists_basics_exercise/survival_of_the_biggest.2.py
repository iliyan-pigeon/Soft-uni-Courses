my_list = input().split(' ')
new_list = list(map(int, my_list))
count = int(input())
for i in range(count):
    smallest_element = min(new_list)
    my_list.remove(str(smallest_element))
    new_list.remove(smallest_element)
print(', '.join(my_list))