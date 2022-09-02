command = input()
courses_data = {}
while command != "end":
    command = command.split(" : ")
    course_name = command[0]
    student_name = command[1]
    if course_name not in courses_data:
        courses_data[course_name] = []
    courses_data[course_name].append(student_name)
    command = input()
for course, students in courses_data.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
        