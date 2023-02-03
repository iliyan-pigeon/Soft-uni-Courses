ranges_number = int(input())
longest_intersection = set()
for i in range(ranges_number):
    first_range, second_range = input().split("-")
    first_start, first_end = tuple(map(int, first_range.split(",")))
    second_start, second_end = tuple(map(int, second_range.split(",")))
    first_set = set(i for i in range(first_start, first_end + 1))
    second_set = set(i for i in range(second_start, second_end + 1))
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
longest_intersection = list(longest_intersection)
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")


