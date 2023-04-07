from functools import wraps


def make_bold(function):

    @wraps(function)
    def wrapped(*args):
        return f"<b>{function(*args)}</b>"

    return wrapped


def make_italic(function):

    @wraps(function)
    def wrapped(*args):
        return f"<i>{function(*args)}</i>"

    return wrapped


def make_underline(function):

    @wraps(function)
    def wrapped(*args):
        return f"<u>{function(*args)}</u>"

    return wrapped


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
