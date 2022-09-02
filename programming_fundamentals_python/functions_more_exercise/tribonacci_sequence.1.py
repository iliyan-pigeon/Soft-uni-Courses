import sys

number = int(input())


def tribonacci_sequence(integer):
    sequence = [1]
    last_numbers = [1]
    while len(sequence) != integer:
        to_add = sum(last_numbers)
        sequence.append(to_add)
        last_numbers.append(to_add)
        if len(last_numbers) > 3:
            last_numbers.pop(0)
    return " ".join(map(str, sequence))


print(tribonacci_sequence(number))