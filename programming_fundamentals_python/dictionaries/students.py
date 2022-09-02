command = input()
students_info = {}
while ":" in command:
    student_data = command.split(":")
    key = student_data[2]
    if key == "programming basics":
        key = "programming_basics"
    id = student_data[1]
    name = student_data[0]
    if key not in students_info:
        students_info[key] = f"{name} - {id}"
    elif key in students_info:
        students_info[key] += "|"f"{name} - {id}"
    command = input()
for key, value in students_info.items():
    if key in command:
        for student in value.split("|"):
            print(student)




