def upper_rhomboid(some_number):
    result = ''

    for i in range(1, some_number + 1):
        current_row = f"{' ' * (some_number - i)}{'* ' * i}"
        if i == some_number:
            result += current_row
        else:
            result += current_row + "\n"

    return result


def lowe_rhomboid(some_number):
    result = ''

    for i in range(some_number - 1, -1, -1):
        current_row = f"{' ' * (some_number - i)}{'* ' * i}"
        result += current_row + "\n"

    return result


number = int(input())
print(upper_rhomboid(number))
print(lowe_rhomboid(number))

