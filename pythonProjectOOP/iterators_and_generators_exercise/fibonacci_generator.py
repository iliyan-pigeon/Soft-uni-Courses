def fibonacci():
    iterations = 0
    number = 0
    old_number = 0

    while True:
        yield number

        if iterations == 0:
            iterations += 1
            number += 1
        else:
            transmitter = number
            number += old_number
            old_number = transmitter



generator = fibonacci()
for i in range(5):
    print(next(generator))