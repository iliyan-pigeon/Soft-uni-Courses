def func_executor(*args):
    result = ''
    for func in args:
        function = func[0]
        data = func[1]
        result += f"{function.__name__} - {function(*data)}\n"
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
