number_of_evaluators = int(input())
name_of_presentation = input()
average_total_grade = 0
combined_total_grade = 0
total_presentations = 0
while name_of_presentation != "Finish":
    combined_grade = 0
    average_presentation_grade = 0
    for evaluator in range(number_of_evaluators):
        grade = float(input())
        combined_grade += grade
    average_presentation_grade = combined_grade / number_of_evaluators
    print(f"{name_of_presentation} - {average_presentation_grade:.2f}.")
    combined_total_grade += average_presentation_grade
    total_presentations += 1
    name_of_presentation = input()
average_total_grade = combined_total_grade / total_presentations
print(f"Student's final assessment is {average_total_grade:.2f}.")


