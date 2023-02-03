students_number = int(input())
student_grades = {}
for i in range(students_number):
    student, grade = input().split()
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))
for student, grades in student_grades.items():
    grades_list = " ".join(str(f"{grade:.2f}") for grade in grades)
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {grades_list} (avg: {average_grade:.2f})")




 