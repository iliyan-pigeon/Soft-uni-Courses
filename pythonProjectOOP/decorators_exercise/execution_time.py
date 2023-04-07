import time


def exec_time(function):

    def wrapped(*args):
        start = time.time()
        function(*args)
        end = time.time()

        return end - start

    return wrapped



@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))