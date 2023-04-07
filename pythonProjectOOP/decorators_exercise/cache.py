def cache(func):

    def wrapped(arg):
        if arg not in wrapped.log:
            wrapped.log[arg] = func(arg)

        return wrapped.log[arg]

    wrapped.log = {}

    return wrapped


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(3))