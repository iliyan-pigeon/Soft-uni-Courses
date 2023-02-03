from collections import deque


def best_list_pureness(numbers_list, rotations):
    numbers_list = deque(numbers_list)
    needed_rotations = 0
    best_pureness = 0
    rotations_made = 0

    for i in range(rotations + 1):
        current_pureness = 0

        for number in range(len(numbers_list)):
            current_pureness += (numbers_list[number] * number)

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            needed_rotations = rotations_made

        numbers_list.appendleft(numbers_list.pop())
        rotations_made += 1

    return f"Best pureness {best_pureness} after {needed_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)