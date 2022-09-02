action_time = int(input())
scenes_number = int(input())
scene_duration = int(input())
preparation_time = action_time * 0.15
time_needed = scenes_number * scene_duration + preparation_time
difference = round(abs(time_needed - action_time))
if time_needed <= action_time:
    print(f"You managed to finish the movie on time! You have {difference} minutes left!")
elif time_needed > action_time:
    print(f"Time is up! To complete the movie you need {difference} minutes.")