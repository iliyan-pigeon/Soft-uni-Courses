bad_grades_tolerance = int(input())
number_bad_grades = 0
average_grade = 0
number_of_problems = 0
grades_total_sum = 0
last_problem = ""
bad_grade_threshold = 4
has_failed = True
while number_bad_grades < bad_grades_tolerance:
    problems_name = input()
    if problems_name == "Enough":
        has_failed = False
        break
    current_grade = int(input())
    if current_grade > bad_grade_threshold:
        number_of_problems += 1
        grades_total_sum += current_grade
        last_problem = problems_name
    elif current_grade <= bad_grade_threshold:
        grades_total_sum += current_grade
        number_of_problems += 1
        number_bad_grades += 1
        last_problem = problems_name
average_grade = grades_total_sum / number_of_problems
if has_failed:
    print(f"You need a break, {number_bad_grades} poor grades.")
elif not has_failed:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
