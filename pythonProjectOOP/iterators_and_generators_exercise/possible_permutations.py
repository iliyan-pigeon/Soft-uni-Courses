from itertools import permutations


def possible_permutations(numbers_list):
    for i in permutations(numbers_list):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]