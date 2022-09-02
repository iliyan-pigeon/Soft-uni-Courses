import math
project_hours_needed = int(input())
available_days = int(input())
workers = int(input())
working_day_hours = 8
overtime_per_worker = 2
education = available_days * 0.1
days_to_work = available_days - education
combined_overtime = workers * (overtime_per_worker * available_days)
hours_to_work = days_to_work * 8 + combined_overtime
difference = abs(math.floor(hours_to_work) - project_hours_needed)
if hours_to_work >= project_hours_needed:
    print(f"Yes!{difference} hours left.")
elif hours_to_work < project_hours_needed:
    print(f"Not enough time!{difference} hours needed.")