students_showed_up = int(input())
average_grade = 0
students_less_than_three = 0
students_less_than_four = 0
students_less_than_five = 0
students_above_five = 0
percent_less_than_three = 0
percent_less_than_four = 0
percent_less_than_five = 0
percent_above_five = 0
combined_grade = 0
for student in range(students_showed_up):
    grade_of_student = float(input())
    combined_grade += grade_of_student
    if grade_of_student < 3:
        students_less_than_three += 1
    elif grade_of_student < 4:
        students_less_than_four += 1
    elif grade_of_student < 5:
        students_less_than_five += 1
    elif grade_of_student >= 5:
        students_above_five += 1
average_grade = combined_grade / students_showed_up
percent_less_than_three = students_less_than_three / students_showed_up * 100
percent_less_than_four = students_less_than_four / students_showed_up * 100
percent_less_than_five = students_less_than_five / students_showed_up * 100
percent_above_five = students_above_five / students_showed_up * 100
print(f"Top students: {percent_above_five:.2f}%")
print(f"Between 4.00 and 4.99: {percent_less_than_five:.2f}%")
print(f"Between 3.00 and 3.99: {percent_less_than_four:.2f}%")
print(f"Fail: {percent_less_than_three:.2f}%")
print(f"Average: {average_grade:.2f}")
