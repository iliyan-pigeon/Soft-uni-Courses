def rounding(numbers: str):
    numbers_list = [round(float(number)) for number in numbers.split()]
    return numbers_list


numbers_as_string = input()
print(rounding(numbers_as_string))
