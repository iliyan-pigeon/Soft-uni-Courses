exam_results = {}
command = input()
while command != "exam finished":
    if "banned" in command:
        student = command.split("-")[0]
        for key, value in exam_results.items():
            for i in value:
                if i == student:
                    exam_results[key].pop(i)
                    break
    elif "banned" not in command:
        student_result = command.split("-")
        name = student_result[0]
        language = student_result[1]
        points = int(student_result[2])
        if language not in exam_results:
            exam_results[language] = {}
            exam_results[language]["submissions"] = 0
        exam_results[language]["submissions"] += 1
        if name not in exam_results[language]:
            exam_results[language][name] = points
        elif name in exam_results[language]:
            if exam_results[language][name] < points:
                exam_results[language][name] = points
    command = input()
print("Results:")
for key, value in exam_results.items():
    for name, points in value.items():
        if name != "submissions":
            print(f"{name} | {points}")
print(f"Submissions:")
for key, value in exam_results.items():
    for name, points in value.items():
        if name == "submissions":
            print(f"{key} - {points}")



