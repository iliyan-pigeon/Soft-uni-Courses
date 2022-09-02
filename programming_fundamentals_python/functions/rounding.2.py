rounding = lambda numbers_like_string: [round(float(number)) for number in numbers_like_string.split()]


numbers_as_string = input()
print(rounding(numbers_as_string))