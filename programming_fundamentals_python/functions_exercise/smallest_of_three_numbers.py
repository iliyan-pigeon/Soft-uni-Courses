import sys


def smallest_number(first, second, third):
    numbers_list = []
    numbers_list.append(int(first))
    numbers_list.append(int(second))
    numbers_list.append(int(third))
    the_smallest = sys.maxsize
    for number in numbers_list:
        if number < the_smallest:
            the_smallest = number
    return the_smallest


first_number = int(input())
second_number = int(input())
third_number = int(input())
the_smallest = smallest_number(first_number, second_number, third_number)
print(the_smallest)

