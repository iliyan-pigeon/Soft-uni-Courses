class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0
        self.number = 0 - self.step

    def __iter__(self):
        return self

    def __next__(self):
        if not self.counter < self.count:
            raise StopIteration

        self.number += self.step
        self.counter += 1
        return self.number


numbers = take_skip(2, 6)
for number in numbers:
    print(number)