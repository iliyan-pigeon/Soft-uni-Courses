lessons_schedule = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    if command[0] == "Add":
        lesson = command[1]
        if lesson not in lessons_schedule:
            lessons_schedule.append(lesson)
    if command[0] == "Insert":
        lesson = command[1]
        index = int(command[2])
        if lesson not in lessons_schedule:
            lessons_schedule.insert(index, lesson)
    if command[0] == "Remove":
        lesson = command[1]
        if lesson in lessons_schedule:
            lessons_schedule.remove(lesson)
        if f"{lesson}-Exercise" in lessons_schedule:
            lessons_schedule.remove(f"{lesson}-Exercise")
    if command[0] == "Swap":
        first_lesson = command[1]
        second_lesson = command[2]
        index_first_lesson = lessons_schedule.index(command[1])
        index_second_lesson = lessons_schedule.index(command[2])
        if first_lesson in lessons_schedule and second_lesson in lessons_schedule:
            transmitter = lessons_schedule[index_first_lesson]
            lessons_schedule[index_first_lesson] = lessons_schedule[index_second_lesson]
            lessons_schedule[index_second_lesson] = transmitter
        if f"{first_lesson}-Exercise" in lessons_schedule:
            index = lessons_schedule.index(first_lesson)
            lessons_schedule.remove(f"{first_lesson}-Exercise")
            lessons_schedule.insert(index + 1, f"{first_lesson}-Exercise")
        if f"{second_lesson}-Exercise" in lessons_schedule:
            index = lessons_schedule.index(second_lesson)
            lessons_schedule.remove(f"{second_lesson}-Exercise")
            lessons_schedule.insert(index + 1, f"{second_lesson}-Exercise")
    if command[0] == "Exercise":
        lesson = command[1]
        exercise = f"{lesson}-Exercise"
        if exercise not in lessons_schedule:
            if lesson not in lessons_schedule:
                lessons_schedule.append(lesson)
                lessons_schedule.append(exercise)
            else:
                index = lessons_schedule.index(lesson)
                lessons_schedule.insert(index + 1, exercise)
    command = input()
for lesson in range(len(lessons_schedule)):
    number = lesson + 1
    lesson = lessons_schedule[lesson]
    print(f"{number}.{lesson}")
