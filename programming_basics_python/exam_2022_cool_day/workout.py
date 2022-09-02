import math

number_of_days = int(input())
kilometres_first_day = float(input())
kilometres_needed = 1000
current_kilometres = kilometres_first_day
total_kilometres = kilometres_first_day
for day in range(1, number_of_days + 1):
    percent_increase = int(input())
    current_kilometres = current_kilometres + (current_kilometres * (percent_increase / 100))
    total_kilometres += current_kilometres
difference = abs(total_kilometres - kilometres_needed)
if total_kilometres >= kilometres_needed:
    print(f"You've done a great job running {math.ceil(difference)} more kilometers!")
elif total_kilometres < kilometres_needed:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(difference)} more kilometers")

