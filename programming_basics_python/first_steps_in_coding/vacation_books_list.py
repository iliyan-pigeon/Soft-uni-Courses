pages = int(input())
pages_per_hour = int(input())
days = int(input())
hours_needed = pages / pages_per_hour
hours_per_day = hours_needed / days
print(round(hours_per_day))