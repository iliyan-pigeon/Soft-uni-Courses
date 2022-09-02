import math
series_name = input()
episode_duration = int(input())
rest_duration = int(input())
lunch_time = rest_duration / 8
chill_time = rest_duration / 4
time_left = rest_duration - (lunch_time + chill_time)
if time_left >= episode_duration:
    left_minutes = abs(time_left - episode_duration)
    print(f'You have enough time to watch {series_name} and left with {math.ceil(left_minutes)} \
minutes free time.')
elif time_left < episode_duration:
    minutes_not_enough = abs(time_left - episode_duration)
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(minutes_not_enough)} more \
minutes.")