from functools import wraps


def even_numbers(function):

    @wraps(function)
    def wrapper(*args):
        numbers = function(*args)
        even_nums_found = [n for n in numbers if n % 2 == 0]
        return even_nums_found

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))