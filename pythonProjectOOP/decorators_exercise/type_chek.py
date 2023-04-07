from functools import wraps


def type_check(data_type):

    def decorator(function):

        @wraps(function)
        def wrapped(*args):
            for arg in args:
                if isinstance(arg, data_type):
                    continue

                return "Bad Type"

            return function(*args)

        return wrapped

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))