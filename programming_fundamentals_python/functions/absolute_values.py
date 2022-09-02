#numbers = [abs(float(number)) for number in input().split()]
#print(numbers)
def abs_float_number(numbers):
    result = [abs(float(number)) for number in numbers]
    return result


numbers = input().split()
print(abs_float_number(numbers))





