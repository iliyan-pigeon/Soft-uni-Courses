import sys

number = int(input())


def tribonacci_sequence(integer):
    sequence = [1]
    last_numbers = [1]
    start_range = sequence[-1]
    while len(sequence) != integer:
        for i in range(start_range, sys.maxsize):
            if sum(last_numbers) == i:
                sequence.append(i)
                last_numbers.append(i)
                if len(last_numbers) > 3:
                    last_numbers.pop(0)
                break
    return " ".join(map(str, sequence))


print(tribonacci_sequence(number))



