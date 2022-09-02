students_number = int(input())
students_grades = {}
for student in range(students_number):
    student_name = input()
    grade = float(input())
    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(grade)
for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")

        