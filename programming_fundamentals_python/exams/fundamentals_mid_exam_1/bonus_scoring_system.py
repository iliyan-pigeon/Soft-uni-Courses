import math

students_number = int(input())
lectures_number = int(input())
additional_bonus = int(input())
highest_bonus = 0
attendances = 0
for student in range(1, students_number+1):
    current_attendance = int(input())
    current_bonus = current_attendance / lectures_number * (5 + additional_bonus)
    if current_bonus > highest_bonus:
        highest_bonus = current_bonus
        attendances = current_attendance
print(f"Max Bonus: {math.ceil(highest_bonus)}.")
print(f"The student has attended {attendances} lectures.")
