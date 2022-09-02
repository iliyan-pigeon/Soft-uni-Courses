import math

number_of_balls = int(input())
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_colours_picked = 0
for ball in range(number_of_balls):
    ball_colour = input()
    if ball_colour == "red":
        total_points += 5
        red_balls += 1
    elif ball_colour == "orange":
        total_points += 10
        orange_balls += 1
    elif ball_colour == "yellow":
        total_points += 15
        yellow_balls += 1
    elif ball_colour == "white":
        total_points += 20
        white_balls += 1
    elif ball_colour == "black":
        total_points /= 2
        total_points = math.floor(total_points)
        black_balls += 1
    else:
        other_colours_picked += 1
print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colours_picked}")
print(f"Divides from black balls: {black_balls}")
