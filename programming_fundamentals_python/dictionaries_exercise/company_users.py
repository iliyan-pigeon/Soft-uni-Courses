command = input()
companies_employees = {}
while command != "End":
    command = command.split(" -> ")
    company = command[0]
    employee_id = command[1]
    if company not in companies_employees:
        companies_employees[company] = []
    if employee_id not in companies_employees[company]:
        companies_employees[company].append(employee_id)
    command = input()
for company, employees in companies_employees.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
