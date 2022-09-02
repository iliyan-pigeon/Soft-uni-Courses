balls_number = int(input())
highest_ball_value = 0
highest_ball_weight = 0
highest_ball_time = 0
highest_ball_quality = 0
for ball in range(balls_number):
    ball_weight = int(input())
    travel_time = int(input())
    ball_quality = int(input())
    current_value = int((ball_weight / travel_time) ** ball_quality)
    if current_value > highest_ball_value:
        highest_ball_value = current_value
        highest_ball_weight = ball_weight
        highest_ball_time = travel_time
        highest_ball_quality = ball_quality
print(f"{highest_ball_weight} : {highest_ball_time} = {highest_ball_value} ({highest_ball_quality}) ")
