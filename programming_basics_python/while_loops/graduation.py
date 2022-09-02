student_name = input()
year = 1
total_grade = 0
average_grade = 0
failed = 0
while year <= 12:
    if failed >1:
        break
    grade = float(input())
    if grade < 4:
        failed += 1
        continue
    year += 1
    total_grade += grade
average_grade = total_grade / 12
if failed < 2:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
if failed >= 2:
    print(f"{student_name} has been excluded at {year} grade")