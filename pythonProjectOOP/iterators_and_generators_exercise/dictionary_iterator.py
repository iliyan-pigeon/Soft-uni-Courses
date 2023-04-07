class dictionary_iter:
    def __init__(self, some_dict):
        self.some_dict = list(some_dict.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.some_dict:
            raise StopIteration

        the_result = self.some_dict.pop(0)
        return the_result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)