class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == self.iterations:
            raise StopIteration

        self.index += 1
        if self.index == len(self.sequence):
            self.index = 0
        self.iterations += 1
        return self.sequence[self.index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

