people = int(input())
capacity = int(input())
courses = 0
while people != 0:
    if capacity == 0:
        break
    courses += 1
    if people >= capacity:
        people -= capacity
    else:
        people = 0
print(courses)
