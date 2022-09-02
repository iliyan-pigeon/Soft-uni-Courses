employees_happiness = [int(happiness) * 3 for happiness in input().split()]
average_happiness = sum(employees_happiness) / len(employees_happiness)
happy_employees = 0
for employee in employees_happiness:
    if employee >= average_happiness:
        happy_employees += 1
if happy_employees >= len(employees_happiness) / 2:
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are not happy!")
