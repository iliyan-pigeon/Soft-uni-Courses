def take_even_numbers(numbers_list: list):
    evens_list = []
    for number in numbers_list:
        if number % 2 == 0:
            evens_list.append(number)
    return evens_list


numbers = [int(number) for number in input().split()]
print(take_even_numbers(numbers))

