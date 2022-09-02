import re


def calculate_points(some_list):
    total_points = 0
    for i in some_list:
        total_points += len(i)
    return total_points


characters = input()
pattern = r"(?<=\=)[A-Z][A-Za-z]{2,}(?=\=)|(?<=\/)[A-Z][A-Za-z]{2,}(?=\/)"
destinations = re.findall(pattern, characters)
print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {calculate_points(destinations)}")


