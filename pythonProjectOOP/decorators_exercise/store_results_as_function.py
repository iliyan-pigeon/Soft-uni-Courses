def store_results(function):

    def wrapped(*args):
        with open("results.txt", "w") as file:
            file.write(f"Function {function.__name__} was called. Result: {function(*args)}")

        return file

    return wrapped


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)