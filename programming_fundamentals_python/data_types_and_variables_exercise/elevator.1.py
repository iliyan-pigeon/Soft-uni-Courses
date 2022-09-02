import math

people = int(input())
capacity = int(input())
courses = 0
if capacity != 0:
    courses = math.ceil(people / capacity)
print(courses)
