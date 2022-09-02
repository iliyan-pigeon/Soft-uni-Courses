def rounding(numbers: str):
    numbers_list = numbers.split()
    new_numbers = []
    for number in numbers_list:
        new_number = round(float(number))
        new_numbers.append(new_number)
    return new_numbers


numbers_as_string = input()
print(rounding(numbers_as_string))
