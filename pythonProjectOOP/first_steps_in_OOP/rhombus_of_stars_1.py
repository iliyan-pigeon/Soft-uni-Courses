def create_rhomboid(some_number):
    result = ''

    def upper_rhomboid():
        upper_result = ''
        for i in range(1, some_number + 1):
            current_row = f"{' ' * (some_number - i)}{'* ' * i}"
            upper_result += current_row + "\n"

        return upper_result

    def lowe_rhomboid():
        lower_result = ''

        for i in range(some_number - 1, -1, -1):
            current_row = f"{' ' * (some_number - i)}{'* ' * i}"
            lower_result += current_row + "\n"

        return lower_result

    result += upper_rhomboid() + lowe_rhomboid()
    return result


number = int(input())
print(create_rhomboid(number))


