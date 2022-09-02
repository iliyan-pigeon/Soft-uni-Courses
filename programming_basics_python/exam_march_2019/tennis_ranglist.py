import math

number_of_tournaments = int(input())
start_points = int(input())
points_from_tournaments = 0
final_points = 0
average_points = 0
wins = 0
percent_wins = 0
for tournament in range(number_of_tournaments):
    stage_in_tournament = input()
    if stage_in_tournament == "W":
        points_from_tournaments += 2000
        wins += 1
    elif stage_in_tournament == "F":
        points_from_tournaments += 1200
    elif stage_in_tournament == "SF":
        points_from_tournaments += 720
final_points = points_from_tournaments + start_points
average_points = points_from_tournaments / number_of_tournaments
percent_wins = wins / number_of_tournaments * 100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_wins:.2f}%")

