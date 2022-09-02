rest_days = int(input())
work_days = 365 - rest_days
rest_day_minutes = 127
work_day_minutes = 63
rest_days_total = rest_day_minutes * rest_days
work_days_total = work_days * work_day_minutes
annual_total_time = rest_days_total + work_days_total
difference = abs(annual_total_time - 30000)
hour = difference // 60
minutes = difference % 60
if annual_total_time > 30000:
    print("Tom will run away")
    print(f"{hour} hours and {minutes} minutes more for play")
elif annual_total_time <= 30000:
    print("Tom sleeps well")
    print(f"{hour} hours and {minutes} minutes less for play")
