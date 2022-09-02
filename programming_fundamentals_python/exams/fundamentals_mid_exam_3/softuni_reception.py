first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_number = int(input())
combined_capacity = first_employee + second_employee + third_employee
hours_answering = 0
rest_counter = 0
while students_number != 0:
    if rest_counter == 3:
        hours_answering += 1
        rest_counter = 0
        continue
    if students_number <= combined_capacity:
        students_number = 0
    else:
        students_number -= combined_capacity
    hours_answering += 1
    rest_counter += 1
print(f"Time needed: {hours_answering}h.")

