import math
number_of_tournaments = int(input())
starting_points = int(input())
final_points = starting_points
number_of_wins = 0
points_from_tournaments = 0
average_points = 0
percent_of_wins = 0
winner_points = 2000
finalist_points = 1200
semi_finalist_points = 720
for tournament in range(number_of_tournaments):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        final_points += winner_points
        points_from_tournaments += winner_points
        number_of_wins += 1
    elif stage_of_tournament == "F":
        final_points += finalist_points
        points_from_tournaments += finalist_points
    elif stage_of_tournament == "SF":
        final_points += semi_finalist_points
        points_from_tournaments += semi_finalist_points
percent_of_wins = number_of_wins / number_of_tournaments * 100
average_points = points_from_tournaments / number_of_tournaments
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_of_wins:.2f}%")