from functools import wraps


def even_parameters(function):

    @wraps(function)
    def wrapped(*args):
        for arg in args:
            if isinstance(arg, int):
                if arg % 2 != 0:
                    return "Please use only even numbers!"
            else:
                return "Please use only even numbers!"

        return function(*args)

    return wrapped


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


